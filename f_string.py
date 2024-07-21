# introduction to f-string
letter="hey my name is {} and i from {}"
country="india"
name="harry"
# it will place the name and country vslue in empty semicolum
print(letter.format(name,country))
# by using f-string
print(f"hry my name is {name} and i am from {country}")

price=49.8999
txt=f"for only {price:.2f} dollars!"
print(txt)
