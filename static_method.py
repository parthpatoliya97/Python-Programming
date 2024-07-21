class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b
# here we have to use self in function arguments to run the function 
a=math(5)
print(a.num)
a.addtonum(6)
print(a.num)
# by calling static method we dont have to use self
print(math.add(5,7))
        