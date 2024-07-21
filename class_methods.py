class employee:
    company="apple"
    name="wilson"
    def show(self):
        print(f"the name is {self.name} and company is {self.company}")
    # here we cant change the company name if we have change the company name we have to use classmethods
    # def changecompany(cls,newcompany):
        # cls.company=newcompany
    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany
e1=employee()
e1.name="william"
e1.show()
e1.changecompany("tesla")
e1.show()
print(employee.company)