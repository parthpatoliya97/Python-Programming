name="hamiltonmasakatza"
fruit="pineapple"
print(len(name))
# here it print including zero but not 4 and it sma for all
# it include 0 th index but not include 4 th index it will run from 0 to 4-1 index
print(name[0:4])
print(name[:4])
# it will print like 0 to 9-2=2 so index is from 0to2
print(fruit[0:-7])
print(fruit[0:len(fruit)-7])
# it will follow index from 8-3 to 8-2 means from 5to6 index
print(fruit[-3:-2])