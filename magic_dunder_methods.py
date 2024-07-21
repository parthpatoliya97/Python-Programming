class employee:
    name="johnsoncharles"
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
e=employee()
print(e.name)
# here ourfunction  method name is __len__ but we print the length by using len name so this magic method
print(len(e))