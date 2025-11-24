import socket
import struct
import dnslib # You might need: pip install dnslib

# Configuration
HOST = 'challs.glacierctf.com'
PORT = 13381
DOMAIN = 'flag.example.com'

def get_flag():
    print(f"[*] Connecting to {HOST}:{PORT}...")
    
    # 1. Construct the DNS Query (TXT Record for flag.example.com)
    q = dnslib.DNSRecord.question(DOMAIN, "TXT")
    q_data = q.pack()
    
    # 2. Add TCP Length Prefix (2 bytes)
    tcp_msg = struct.pack("!H", len(q_data)) + q_data
    
    # 3. Send over TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(tcp_msg)
    
    # 4. Read Response Length (First 2 bytes)
    len_bytes = s.recv(2)
    if not len_bytes:
        print("[-] No response.")
        return
    resp_len = struct.unpack("!H", len_bytes)[0]
    
    # 5. Read the DNS Packet
    resp_data = b""
    while len(resp_data) < resp_len:
        chunk = s.recv(resp_len - len(resp_data))
        if not chunk: break
        resp_data += chunk
    s.close()
    
    # 6. Parse Response
    parsed = dnslib.DNSRecord.parse(resp_data)
    print(f"[*] Status: {dnslib.RCODE[parsed.header.rcode]}")
    
    if parsed.rr:
        print("[*] Extracting TXT data...")
        full_data = b""
        for rr in parsed.rr:
            # dnslib stores TXT data as a list of bytes
            for chunk in rr.rdata.data:
                full_data += chunk
        
        # Save to file
        with open("final_flag.png", "wb") as f:
            f.write(full_data)
        print(f"[+] Saved {len(full_data)} bytes to final_flag.png")
        print("[*] Open 'final_flag.png' to see the flag!")
    else:
        print("[-] No Answer section found.")

if __name__ == "__main__":
    get_flag()