"""
length, breadth =input().split()
length = int(length)
breadth = int(breadth)
area =length*breadth
"""

a = int(input("enter a value:"))
if a<=20:
    print("given value is less then 20")

b = int(input("enter b value"))
if a<=50:
    print("big value")
else:
    print("less value")

# to check multiple conditions then use elif  statement

c = int(input("enter week day"))
if c==1:
    print("it's monday")
elif c==2:
    print("it's tuesday")
elif c==3:
    print("it's wednesday")
elif c==4:
    print("it's thursday")
elif c==5:
    print("it's friday")
elif  c==6:
    print("it's saturday")
elif c==7:
    print("it's sunday")
else:
    print("invalid data")