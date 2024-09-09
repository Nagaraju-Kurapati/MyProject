# set {}
# sets are unordered means while printing the sets order will be changing
#sets are not follow the index --there is no order then no index
# sets are not mutable means not change
#here we can't edit or update the exist values in set but we can add and remove the elements
#dupllicates also not allowed.

s ={2,44.4,789,"ram"}
print(s)
print(len(s))
#print(s[0])
print(s.add("laxman"))
print(s)
print(s.remove("laxman"))
print(s)
# if you try to remove value that's not present then shows the error


for i in s:
    print(i)
