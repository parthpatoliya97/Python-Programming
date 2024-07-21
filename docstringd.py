def square(n):
    # we must have to put docstring righy below the function name and right beloe the function body
    '''takes in a number n,returns the square of n'''
    print(n**2)
square(5)
# if we change the comments we cant change the program but if we change the docstring it will the change the program function
print(square.__doc__)