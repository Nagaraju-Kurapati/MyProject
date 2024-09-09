# function is nothing but it's a block of code and it's perform the particular task

#exam 1
def add(a,b):
    c=a+b
    print("sum is{}".format(a,b))
    print(c)

add(20,40)

#example 2
def great(name):
    print("Hi {}".format(name))
    print("how are you?")

great("ram")

#example 3
def results(marks):
    if marks >=75:
        print("first class")
    elif marks <=50:
        print("Second class")
    else:
        print("fail")

results(80)

#example 4

def area_of_rectangular(l,b):
    area=l*b
    print(area)

area_of_rectangular(20,20)

#example 5

def area_of_triangle(b,h):
    res = 0.5 *b*h
    print(res)

area_of_triangle(4,8)

