#list is nothing but collection of different data types
from operator import index

l =[1,2,3,4,"ram"]
print(type(l))
# list have some properties
# list is ordered
# example list l is stored values in ordered
# list is indexed
print(l[0])
print(l[4])
print(l[-1])

# list allow's duplicates
# list is mutable
# mutable means changes

#slicing
print(l[1:3])

print(1 in l)
print(8 in l)

# adding the new value in existing value position in list
l.insert(1,"sagar")
print(l)
#appender adding the values in last
l.append("laxman")
print(l)

#Nested list:

#With in the list create another list is called "Nested list"
numbers=[1,34,67,89,[90,33.4,44,"ram"],17,0]

print(numbers[0])
print(numbers[3])
print(numbers[4])
print(numbers[4][1])
print(numbers[-2])
print(numbers[4][:])
print(numbers[4][-1])


# we also join the two lists
a =[23,45,68,'ram']
b =[67,89,90,'laxman']
print(a.extend(b))
print(a)

