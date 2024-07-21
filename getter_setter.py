class myclass:
    def __init__(self,value) :
        self.value=value
    def show(self):
        print(f"value is {self.value}")
    @property
    def ten_values(self):
        return 10*self.value
    
    @property.setter
    def ten_values(self,new_value):
        self.value=new_value/10
        return 10*self.value
obj=myclass(10)
obj.ten_values=67
print(obj.ten_values)
obj.show()