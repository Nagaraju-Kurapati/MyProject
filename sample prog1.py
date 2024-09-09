

#area of triangle
l, b =input("enter the values: ").split()
l = int(l)
b = int(b)
area =l*b
print(area)


#conditions
age=input("enter your age: ")
age = int(age)
if age >=18:
    print("major")
elif age <=18:
    print("child")
elif age >=60:
    print("old")
else:
    print("invalid data")

#swapping
a=10
b=20
temp=a
a=b
b=temp
print(a,b)

#pattern
n =5
for i in range(n):
    p=1
    for j in range(i+1):
        print(p, end=" ")
        p+=1
    print()