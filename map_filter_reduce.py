def cube(x):
    return x*x*x
l=[1,2,3,4,5,6]
# without ussong map function
# newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)

# map filter reduce are higher order function because all of are take function as a argument 

# by using map function

# here we can also use lambda function rather than writting function
newl=list(map(cube,l))
print(newl)

# by using filter function
def filter_function(a):
    return a>2
newnewl=list(filter(filter_function,l))
print(newnewl)

from functools import reduce
# reduce function
numbers=[1,2,3,4,5]
# it is work like this type
# first it is sum 1 and 2 [3.3.4.5]
# than it will sum 3 and 3 [6.4.5]
# than it will sum 6 and 4 [10.5]
# than it will sum 10 and 5 [15]
# calculate sum of number sby using reduce function
def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)
print(sum)