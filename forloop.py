colors =["red","green","blue","yellow"]
for color in colors:
    print(color)
    for i in color:
     print(i)
    
for k in range(1,10):
   print(k)

for k in range(1,12,3):
   print(k)
for k in range(1,26,4):
   print(k)

# break statement
for i in range(12):
   if(i==10):
      break
   print("5x",i+1,"=",5*(i+1))
print("loop ko chod ke nikal gaya")
  