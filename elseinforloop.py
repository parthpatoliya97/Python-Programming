# here loop will run till i==5 and else ststement is also executed
for i in range(5):
    print(i)
else:
    print("sorry no i")

for i in []:
    print(i)
else:
    print("sorry no i")
# here loop woll run till i==4 and here else is not executed
for i in range(6):
    print(i)
    if(i==4):
        break
else:
    print("sorry no i")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block out of loop")