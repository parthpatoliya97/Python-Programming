a=int(input("enter the number:"))
print(f"pritn the multiplication table of {a} is:")
try:
    for i in range(11):
        print(f"{int(a)} x {i} = {int(a*i)}")
except ValueError:
    print("invalid input")
    print("end of program")

try:
    print(10/0)
except:
    print("can't divide by zero")
# finally exception handling
try:
    l=[1,5,6,7]
    i=int(input("enter the index:"))
    print(l[i])
except:
    print("some error occured")

print("i am always executed")

def func1():
    try:
     l=[1,5,6,7]
     i=int(input("enter the index:"))
     print(l[i])
     return 1
    except:
        print("some error occcured")
        return 0
    finally:
        print("ia am always exexuted")