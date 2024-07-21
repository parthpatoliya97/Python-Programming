class employee:
    def __init__(self,name,id) :
        self.name=name
        self.id=id
    def showdetails(self):
        print(f"the employee name is {self.name} and id is {self.id}")

class programmer(employee):
    def showlanguage(self):
        print("the default language is python")

emp=employee("part",114)
emp.showdetails()
e2=programmer("harry",115)
e2.showdetails()
e2.showlanguage()

# single inheritance
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("sound made by the animal")
class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self,name,species="dog")
        self.breed=breed
    def make_sound(self):
        print("bark!")
        
d=dog("dog","doberman")
d.make_sound()

a=animal("dog","pitbull")
a.make_sound()

# multiple inheritance
class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"the name is {self.name}")
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"the dance is {self.dance}")
class danceremployee(employee,dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
o=danceremployee("kathak","shivani")
print(o.name)
print(o.dance)
print(danceremployee.mro())

# multilevel inheritance
# hybrid and hierarchical inheritance

