def calculatesum(a,b):
    sum=a+b
    print(sum)

def isgreater(a,b):
 if(a>b):
  print(a)
 else:
  print(b)

a=5
b=3
calculatesum(a,b)
isgreater(a,b)

c=8
d=7
calculatesum(c,d)
isgreater(c,d)

calculatesum(a=10,b=20)

def average(*numbers):
  sum=0
  for i in numbers:
    sum=sum+i
  return sum/len(numbers)

g=average(5,6,7,1)
print(g)