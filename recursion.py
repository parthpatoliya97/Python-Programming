def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(3))

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    
n=int(input("enter the range of the numbers\n: "))
for n in range(0,n):
    print(fibonacci(n))
