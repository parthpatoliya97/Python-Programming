class parentclass:
    def parent_method(self):
        print("this is the parent class")

# it way of writting inheritance 
class childclass(parentclass):
    def child_method(self):
        super().parent_method()
        print("this is the child class")

child=childclass()
child.child_method()

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang=lang

# rohan=employee("rohan das",420)
parth=programmer("parth",420,"python")
print(parth.name)
print(parth.id)
print(parth.lang)

        