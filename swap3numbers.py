#swapping without using third variable
num1=int(input("enetr the first number:"))
num2=int(input("enetr the second number:"))
print("before swapping:")
print("num1=",num1)
print("num2=",num2)
num1,num2=num2,num1
print("after swapping:")
print("num1=",num1)
print("num2=",num2)
#swappinf using arithmetic operators
num1=int(input("enetr the first number:"))
num2=int(input("enetr the second number:"))
print("before swapping:")
print("num1=",num1)
print("num2=",num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("after swapping:")
print("num1=",num1)
print("num2=",num2)
#swapping using third variable
num1=int(input("enetr the first number:"))
num2=int(input("enetr the second number:"))
print("before swapping:")
print("num1=",num1)
print("num2=",num2)
temp=num1
num1=num2
num2=temp
print("after swapping:")
print("num1=",num1)
print("num2=",num2)