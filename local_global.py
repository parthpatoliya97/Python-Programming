x=10

def my_function():
    global x
    x=4
    y=5
    print(y)

my_function()
print(x)      
# print(y) is not possible because it is only accesible for the only in the function area out of the function it is not accesible