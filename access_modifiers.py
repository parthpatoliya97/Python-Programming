class employee:
    def __init__(self):
        self.__name="johnson"
# print(a.name) cannot be accesed directly
a=employee()
# can be accesed directly
print(a._employee__name)

        