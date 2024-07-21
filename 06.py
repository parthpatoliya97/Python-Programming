nm="!!djsnake!!!!"
ab="james"
ms="harry john roman brock"
ph="hi python how are you"
print(nm)
print(nm.upper())
print(nm.lower())
# it will discard/delete "!" type char in the string not effect the begining char
print(nm.rstrip("!"))
print(ab.replace("james","johny"))
# it simply takes all the string in the on box
print(ms.split())
# it capitalize the only first charachter of teh string
print(ph.capitalize())
# it simply counts how many times the h is exists in the string
print(ph.count("h"))
# it simply check that string is ends with "!!!!"
print(nm.endswith("!!!!"))
str="welcome to console"
# it will check if at the end of string from 4 to 10 is to is at the end
print(str.endswith("to",4,10))
# it will find the index where to exists
print(str.find("to"))
str1="WelcomeToTheConsole"
print(str1.isalnum())
str2="Welcome"
print(str2.isalpha())
# it checks that all the characters in the string are small or not
print(str2.islower())
abd="welcome to java"
abdv="welcome to java\n"
# it simply checks if the string is printable or not
print(abd.isprintable())
print(abdv.isprintable())
p1="        "
# it simply checks if there is any space in string
print(p1.isspace())
p2="World Health Organization"
# it checks that each first word of the string is capital 
print(p2.istitle())
p3="hello HOW are you JAVA"
# it converts all lower letters to capital and capital letters to small
print(p3.swapcase())
p4="david beckham leon messi"
# it sets all the first letters of each word in the capital
print(p4.title())
