class person:
    # it is a way of initiate constructor in python
    def __init__(self,n,o):
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("harry","developer")
b=person("divya","HR")
a.info()
b.info()