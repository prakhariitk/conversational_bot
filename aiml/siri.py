import aiml
import numpy as np
import os
record=open('record.txt' , 'r')
ask=input("hi there are you new customer . reply with (yes/no)?" )
if ask=='yes':
	unique_id=0
	for x in record:
		unique_id+=1
	record.close()
	record=open("record.txt","w")	
	record.write(str(unique_id))
	print(input("enter your name>>"))
	record.write(str(input) + "\n")
	print("your unique id is " ,unique_id)
else:
	ask=input("enter your unique_id :")
	unique_id=int(ask)
record.close()


# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
   	print(kernel.respond(input("enter you message>>>")))
