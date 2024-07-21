def my_generator():
    for i in range(50):
        yield i
gen=my_generator()
# here the value is generated when it is called it is not stored like list
# print the value by without using loop
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# for j in gen:
#     print(j)
