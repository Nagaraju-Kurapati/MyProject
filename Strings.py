#Strings:
a = "Cognine Technologies"
print(type(a))

# positive index
print(a[0])
print(a[1])

# negative index also possible
print(a[-0])
#print length of a
print(len(a))

#concatination of strings
b="naga"
c="raju"
d=b+c
print(d)
e=b+" "+c
print(e)

#iterating the string using for loop
#\n = new line
#\t = one space
for i in b:
    print(i,end=" ")

# in and not in
# check the particular character present or not
print('n' in b,end="\n")
print("a" not in b)

# format function
name =input("enter your name: ")
print("Hi {}, how are you?".format(name))

# lowe and upper functions
print(a.upper())
print(a.lower())

#split function
#find function