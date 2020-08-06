def Fib(n):
   if n<=1:
       return n
   else:
       return (Fib(n-1)+Fib(n-2))

num=int(input("Enter the terms:"))
if num<=0:
    print("Please enter a positiv e integer.")
else:
    print("Fibonacci Sequence:")
    for i in range(num):
        print(Fib(i))