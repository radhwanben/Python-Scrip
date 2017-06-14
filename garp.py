import socket

logo='''
**********************************************************
IIIIIIIIIIIIIIIIIIIIII
I     _       _      I    	{**Coded By Radhwan ben youssef**}
I    W_W     W_W     I  	{**greetz to alah**}
I       ....         I
IIIIIIIIIIIIIIIIIIIIII
      IIIIIIIIIIII
      IIIIIIIIIIII
IIIIII          IIIIIII
IIIIII      	IIIIIII
IIIIIIIIIIIIIIIIIIIIIII
-----------------------	
**********************************************************'''
print(logo)
hostname =raw_input("enter hosts list plz ...\n")
w = open(hostname,"r")
for i in w.readlines():
	i.replace('http://',"")
	i=i.rstrip("\n")
	IPHOLDER = socket.gethostbyname(i)
	print(IPHOLDER )
	
