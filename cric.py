import random

import sys

print("\t\t  ",chr(9989),"Possible inputs")

print("\t\t    ",chr(10122),chr(10123),chr(10124),chr(10125),chr(10126),chr(10127),"\n")

print("\t\t\t",chr(10070),chr(10070),chr(10070))

print("\t\tLet's begin with the TOSS")

print("1.head")

print("2.tail\n")

a=int(input())

b=random.randint(1,2)

if a==b:

	print("\t\t\t",chr(10070),chr(10070),chr(10070))

	print("\t\tyou won the toss and decided to",chr(10067),"\n")

	print("1.Bat") 

	print("2.Bowl\n")

	a=int(input())

	if a==1:

		case=1

		print("\t\tYou elected bat first")

		print("\t\t\tLET'S PLAY!")

	else:

		case=2

		print("\t\tYou elected bowl first")

		print("\t\t\tLET'S PLAY!")

else:

	print("\t\t\t",chr(10070),chr(10070),chr(10070))

	print("\tcomputer won the toss and elected to bat")

	print ("\t\t\tLET'S PLAY!")

	case=2

score=0

wkt=5

def bat(a):

	global score,wkt

	if a>6:

		print("invalid input entered GAME OVER!")

		sys.exit()

	b=random.randint(1,6)

	if a==b:

		print("\nthat's out! ",chr(10062))

		wkt-=1

		print(score,"-",(5-wkt),"\n")

	else:

		score+=a

		print("score:",score)

def bowl(a):

	global score,wkt

	if a>6:

		print("invalid input entered GAME OVER!\n\n\n")

		sys.exit()

	b=random.randint(1,6)

	if a==b:

		print("\nthat's out!",chr(10062))

		wkt-=1

		print(score,"-",(5-wkt),"\n")

	else:

		score+=a

		print("computer:",score)	

if case==2:

	while wkt>0:

		a=int(input())

		bowl(a)

		if wkt==0:

			print("\t\t\tALL OUT!",chr(9757))

			print("\t\tfirst innings score:",score,"-",(5-wkt))

	trgt=score+1

	print("\t\t    your target is",trgt)

	print ("\t\t\tLet's begin")

	score=0

	wkt=5

	while wkt>0:

		a=int(input())

		bat(a)

		if score>trgt:

			print("\t",chr(9889),"you beat computer by",wkt,"wickets",chr(9889),"\n\n\n")

			break

		if wkt==0:

			req=trgt-score

			reqrd=req-1

			print("\t\t",chr(9889),"computer won by",reqrd,"runs",chr(9889),"\n\n\n")

			

if case==1:

	while wkt>0:

		a=int(input())

		bat(a)

		if wkt==0:

			print("\t\t\tALL OUT!",chr(9757))

			print("\t\t  your score:",score,"-",(5-wkt))

	trgt=score+1

	print("\t\ttarget for computer is:",trgt)

	print("\t\t\tLet's begin")

	score=0

	wkt=5

	while wkt>0:

		a=int(input())

		bowl(a)

		if score>trgt:

			print("\t",chr(9889),"computer beat you by",wkt,"wickets",chr(9889),"\n\n\n")

			break

		if wkt==0:

			req=trgt-score

			reqrd=req-1

			print("\t\t",chr(9889),"you won by",reqrd,"runs",chr(9889),"\n\n\n")
