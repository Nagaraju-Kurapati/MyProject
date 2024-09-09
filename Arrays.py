import array as arr

a=arr.array("d",[1,2,3,4.5])
print(a)
#adding value
a.append(8.5)
print(a)
#extend the array list
a.extend([9.0,99])
print(a)
#remove value in array
print(a.pop(3))
print(a)