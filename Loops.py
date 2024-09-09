#loops
#range
for x in range(5):
    print(x)
# here 2 is used fo jumping the numbers
for y in range(1,5,2):
    print(y)

#while loop:
n=10
while(n>0):
    print(n,end=" ")
    n=n-1
print("while loop with continue statement")
#while loop with continue:
i= 0
while(i<5):
    if i==2:
        i=i+1
        continue
    print(i)
    i=i+1

#while loop with break statement:
print("while loop with break statement")
j=0
while(j<10):
    if j==6:
        j=j+1
        break
    print(j)
    j=j+1


print("for loop with continue statement")
#for loop with continue statement
# here continue is skip the value and continue the remin conditions
for k in range(1,10):
    if k==5:
        continue
    else:
        print(k,end=" ")


print("for loop with break statement")
for l in range(1,100):
    if l==50:
        break
    else:
        print(l, end="-")


# for loop
print("for loop")

a =int(input("enter a value: "))
value=0
for a in range (1,a+1):
    if a%2==0:
        value =value+a
print(value)



#identify the even odd numbers
z =str(input("enter z value: "))
even = 0
odd = 0
for p in z:
    if int(p)%2==0:
        even =even+int(p)
    else:
        odd =odd+int(p)

print(even,odd)