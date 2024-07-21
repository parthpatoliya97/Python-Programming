import random
arr=random.randint(0,10)
print(arr)

# it will print only even value between 100 to 200
num=random.randrange(100,200,2)
print(num)

# it will generate float value between 50 to 70
num=random.uniform(50,70)
print(num)

# if we want to print random list of numbers
# numlist=random.sample(range(10,110),30)
numlist=random.sample(range(1000,2000),700)
numlist.sort()
print(numlist)
