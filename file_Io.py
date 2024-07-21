# it is used to print binary format of string
f=open("myfile.txt","rb")

# it is used to print text format of string
f=open("myfile.txt","rt")


# readning a file
print(f)
f=open("myfile.txt","r")
text=f.read()
print(text)
f.close()

# wtitting a file
f=open("myfile.txt","w")
f.write("hello world")
f.close()

# append the text in the file
f=open("myfile.txt","a")
f.write("hello world")
f.close()

# with the help of with statement we dont have to close the file
with open("myfile.txt","a") as f:
    f.write("hey i am inside the file")

# read lines from the text file
f=open("myfile.txt","r")
while True:
    line=f.readline()
    if not line:
        break
    print(line)

# print the student marks by usimg split function,readlines method
f=open("myfile.txt","r")
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"marks of students {i} in maths is : {m1}")
    print(f"marks of students {i} in chemistry is : {m2}")
    print(f"marks of students {i} in physics is : {m3}")
    print (line)

# writelines method it will chanhe the new lines and change the old lines in text file
f=open("myfile.txt","w")
lines=["line 1\n","line 2\n","line 3\n"]
f.writelines(lines)
f.close()


# seek() method
with open("myfile.txt","r")as f:
    print(type(f))
    # move the 10th byte in the file means it will start read the character form the particular character position
    f.seek(10)
    # resd the next five bytes
    # tell() function is used to track the current position in the file
    print(f.tell())
    data=f.read(5)
    print(data)

    # truncate() function is used to cut the some function and print the truncate portion
    with open("myfile.txt","w")as f:
        f.write("hello world")
        f.truncate(5)
   