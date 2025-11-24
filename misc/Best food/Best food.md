![alt text](image.png)

This challenge was my favourite by far it was to find the flag in the reviews of a restaurant that you have to find using a rust program they gave you.

First i used the rust file it was given to find out the center points of bars, ATMs, taxi stands, in a city (the CTF location → Graz), then triangulating a final location using distances.

I got 
bar_dist  = 0.6412652119499
atm_dist  = 0.2822972577454
taxi_dist = 0.9572772921063

The solve.py file when run will ask you info 
![alt text](image-1.png)

I got the final coordinates and went to google maps to find the restaurant 

![alt text](image-2.png)

Near it was this Grill&Box
![alt text](image-3.png)

In the reviews found this base64 txt
![alt text](image-4.png)

And converting it you find the flag