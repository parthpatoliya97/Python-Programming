# sets do not print repeated items 
s={2,4,2,6}
print(s)
# printing orfer is not matter means it will print diffrent values 
info={"carela",19,"false",5,9,19}
print(info)

s1={1,2,5,6}
s2={8,7,9,5}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
s3=s1.intersection_update(s2)
print(s3)

cities={"tokyo","madrid","berlin","delgi"}
cities2={"tokyo","berlin","spain","usa"}
cities3=cities.symmetric_difference(cities2)
print(cities3)

# disjoint function is used to find that if there is no similar element in both the sets
cities={"tokyo2","madrid","berlin3","delgi"}
cities2={"tokyo","berlin","spain","usa"}
print(cities.isdisjoint(cities2))

# superset
cities={"tokyo","madrid","berlin","delgi"}
cities2={"tokyo","berlin"}
print(cities.issuperset(cities2))
print(cities2.issubset(cities))


