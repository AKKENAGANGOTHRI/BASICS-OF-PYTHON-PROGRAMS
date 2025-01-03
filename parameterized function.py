#example for parameterized function
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a//b
sum=add(20,40) 
print(sum) 
difference=sub(25,10)
print(difference)
product=multiply(2,5)
print(product)
quotient=divide(20,50)
print(quotient)
print("===================================================")
def display(n):
    print("i'm the function one")
    n()
def one():
    print("i'm first nested function")
def two():
    print("i'm seconf nested function")
display(one)
display(two)