l=[1,5,3,8,9,21,15,4]
print(l)
l.sort()
print(l)
l.append(7)
print(l)
# it will copy the content of list l
# we cant write 
# m=l but we can write the copy list of l that is given below
m=l.copy
print(l)
l.insert(1,299)
print(l)
m=[253,133,183]
# it will join the list m behind the list of l 
l.extend(m)
print(l)
k=l+m
# similarly it will also print the or join the list l with list m
print(k)