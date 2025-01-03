def add(a,b):#formal argument
    c=a+b
    print(c)
add(2,5)#actual argument
print()
#positional arguments
def pw (x ,y):
    z=x ** y
    print(z)
pw (5, 2)
print()
#key word 
def show(name,age):
    print(name,age)
show(name='sai',age=23)
print()
 #default
def d(name,age=12):
    print(name,age)
d(name='raj',age=45)
print()
#variable length
def add(*num):
    z=num[0]+num[1],num[2]
    print(z)
add(5,4,2)
print()
#keyword variable length 
def a(**num):
    z=num['a']+num['b']
    print(z)
a(a=5,b=2)