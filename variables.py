#variables nothing but container which, can be store the values
#when ever you want to use those values then directly call that variable
#variables allways starts with letters and underscore symbol (_)
#And variables shouldn't start with the numeric numbers
#And here abc, ABC --> both are different

#data types: The data types allways tells that which type of values you want store in the variable.

x = 5
y = "John"
z='Cognine Technologies'
print(z)
print(x)
print(y)
#or
print(x,y,z)
#using the end mention the spaces
print(y,end='')
print(z)
#also using seperator
print(y,z,sep='-')
#'\n' --> next line
#\t --> tab space


a=10
b='''Cognine'''
_ram=23.45
_123abc=4567

print(a)
print(b)
print(_ram)
print(_123abc)
print (type(a))

#Type Casting
#Implicit Type Casting:
#Implicit conversion also called as Automatic type conversion.
ram = 5
#Explicit Type Casting:
#If we wantedly change the data type for particular variable That is called Explicit type casting.
print(type(ram))

laxman = str(ram)
print(type(laxman))

s='ram'
d=2
m=s*d
print(type(m))

"""
Comments:
Interpreter ignore the these comments.
These Comment lines are not executed.
Single line comments;
#-------------------------------
Multi line comment:
"""

dev = 3.14
print(type(dev))
print(dev)
nag = int(dev)
print(type(nag))


#input
#when ever the taking input values and those values allways datatype is string
num1 = input("pls enter the first number =") #5
num2 = input("pls enter the second number =") #5

print(num1,num2,end='\n')
res=(num1+num2)
print(res) #here result should be 55
#because the input values datatype allways string
#here concat the two string like 5+5 =55
#in this case we need to convert the datatype string to int by using the type casting method
num1=int(num1)
num2=int(num2)
res=num1+num2

print(res)
