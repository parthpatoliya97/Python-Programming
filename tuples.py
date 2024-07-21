# introduction to tuple
tup=(1,2,76,342,32,"green")

print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

if 3421 in tup:
    print("yes 3421 is present in this tuple")
else:
    print("3421 is not present in the tuple")
tup2=tup[1:4]
print(tup2)

countries =("spain","italy","india","england","germany")
temp =list(countries)
temp.append("russia")
temp.pop(3)
temp[2]="finland"
countries =tuple(temp)
print(countries)

tup1=(0,1,2,3,2,3,1,3,2,3)
res=tup1.index(3,4,8)
print("count of 3 in tuple is :",res)