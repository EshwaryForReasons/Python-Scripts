# importing the required module 
import matplotlib.pyplot as plt
import matplotlib as mpl
import time

def largest(arr,n): 
    max = arr[0] 

    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max

print("Welcome to the prime number calculator")
i1 = input("What is the first number")
i2 = input("What is the second number")

l = int(i1)
u = int(i2)

print("Prime numbers between", l, "and", u, "are:") 

primeNumbers = []
x = []

for num in range(l, u + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           primeNumbers.append(num)

v = len(primeNumbers)
v1 = largest(primeNumbers, v)
rn = 0

for num in range(0, v):
    x.append(rn)
    rn = rn + 1

mpl.style.use("seaborn")
plt.scatter(x, primeNumbers, color="red") 

plt.xlabel('Numbers For Some Reason') 
plt.ylabel('Prime Numebers') 
plt.title('Prime Numbers') 

plt.show() 
