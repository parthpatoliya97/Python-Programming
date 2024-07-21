class employee:
    company_name="apple"
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
    def showdetails(self):
        print(f"the name of the employee is {self.name} and the raise amount in {self.company_name} is {self.raise_amount}")
#here the instance variable is emp1 if we chnage the instance variable value it will change the old value otherwise it will show us local value
emp1=employee("harry")
emp1.raise_amount=0.3
emp1.company_name="google"
emp1.showdetails()

emp2=employee("johnson")
emp2.raise_amount=0.5
emp2.company_name="amazon"
emp2.showdetails()

emp1=employee("prince")
emp1.showdetails()


        