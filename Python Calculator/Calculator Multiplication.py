import time
import clipboard

print("Welcome to the multiplication calculator")
p = input("Which profile would you like?")
pi = int(p)

#multiply two digit numbers
def calculator():
	i1 = input("What is the first number?")
	i2 = input("What is the second number?")

	v = int(i1) * int(i2)

	print(v)
	clipboard.copy(v)

	ri = input("reset?")

#multiply by 11
def clac_profile1():
	i1 = input("What is the number?")

	v = int(i1) * 11

	print (v)
	clipboard.copy(v)

#multiply by 111
def clac_profile2():
	i1 = input("What is the number?")

	v = int(i1) * 111

	print (v)
	clipboard.copy(v)

#multiply by 111
def clac_profile3():
	i1 = input("What is the number?")

	v = int(i1) ** 3

	print (v)
	clipboard.copy(v)

if pi == 0:
	while True:
		calculator()
elif pi == 1:
	while True:
		clac_profile1()
elif pi == 2:
	while True:
		clac_profile2()
elif pi == 3:
	while True:
		clac_profile3()