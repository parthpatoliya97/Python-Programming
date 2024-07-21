# by using dir method it give information about object
# x=(1,2,3)
# print(dir(x))
# print(x.__add__)


# by using __dict__ method it give attribute as a dictionary format
class person:
    def __init__(self,name,age): 
        self.name=name
        self.age=age   
p=person("john",30)
print(p.__dict__) 

# ny using help it give hint 
print(help(person))