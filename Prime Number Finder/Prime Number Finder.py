import time

print("Welcome to the prime number calculator")
i1 = input("What is the first number")
i2 = input("What is the second number")

l = int(i1)
u = int(i2)

print("Prime numbers between", l, "and", u, "are:")

for num in range(l, u + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

time.sleep(10000)