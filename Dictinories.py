#dictinories
#it's a collection of key value pairs or property name and property data
d ={"name":"ram","class":5,"marks":80}
print(d)
print(type(d))
print(len(d))
# Python 3.7 and later
#print(d[0])
#print what property name you want
print(d.get("class"))
#dictinories ordered
#and follows index also
#mutable also means changes
# and not allow duplicates


# in and not in
print("name" in d)

# here we update the values also using update function
#d.update({"class":6})
#print(d)
print(d.update({"class":6}))

#adding the values also
d["subject"]=["english"]
print(type(d))

#list
print(type(d.get("subject")))

#also we remove the pair values
d.pop("subject")
print(d)

dict_1= {'apple': 1,'banana': 2,'cherry': 3}
print(len(dict_1))

print(dict_1.get("apple"))

for key, value in dict_1.items():
    print(f"{key}: {value}")


x=d.items()
print(x)
#here onlu values moved to anthoer varable
y=d.values()
print(y)

#Nested dictinories:

#declare the dictinory with in the another dictionary is called Nested dictinories.

student_data={"ram":{"roll_num":10,"age":20,"course":"phy"},
    "laxman":{"roll_num":12,"age":22,"course":"java","phone":9498}}

print(student_data)
print(student_data["ram"])
print(student_data["laxman"]["age"])

#adding one more key pair
student_data["ram"]["mobile_number"]="234567"
print(student_data)

#deleting
del student_data["ram"]["mobile_number"]
print(student_data)

#use pop also we can delete

student_data["ram"].pop("course")
print(student_data)