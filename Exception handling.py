# we can use try and except, finally
from typing_extensions import Final

a=10
b=0
try:
    c=a/b
    print(c)
except:
    print("b value can't be zero")


#try and finally

l=input("enter the l value: ")
m=input("enter the m value: ")

try:
    if l>m:
        print("l value is bigger")
finally:
    print("invalid data") # exception is occurs or not but finally block allways executed


#try & except & else

marks=input("enter the marks: ")
marks=int(marks)
try:
    if marks >=75:
        print("first class")
except:
    if marks >=50:
        print("second class") # if exception occurs then except block only executed.
else:
    print("fail") # here no exception try bloc will executed and else block also executed
