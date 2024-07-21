class person:
    name ="harry"
    occupation="harry"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()

a.name="shubham"
a.occupation="accountant"

b.name="nitika"
b.occupation="HR"

c.name="joy"
c.occupation="gamer"

a.info()
b.info()
c.info()