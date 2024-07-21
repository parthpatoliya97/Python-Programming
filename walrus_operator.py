# walrus operator

# example:1
# numbers=[1,2,3,4,5]
# while(n :=len(numbers))>0:
#     print(numbers.pop())

# example:2
# without walrus operator
# foods=list()
# while True:
#     food=input("what food do you like? :")
#     if(foods=="quit"):
#         break
#     foods.append(food)

# with walrus operator
# foods=list()
# while(food :=input("what food do you like? :"))!="quit":
#     foods.append(food)