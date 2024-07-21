x=int(input("enter value of x"))
match x:
    case 0:
        print("the x is zero")
    case 1:
        print("the x is 4")
    case _:
        print(x)

y=int(input("enter value of y"))
match y:
    case _ if y!=90:
        print(y,"is not 90")
    case _ if y!=80:
        print(y,"is nor 80")
    case _:
        print(x)