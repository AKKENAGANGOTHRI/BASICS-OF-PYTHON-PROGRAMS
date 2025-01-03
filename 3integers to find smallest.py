#to find the smallest number for 3 integers
num1=int(input("enter the integer:"))
num2=int(input("enter the integer:"))
num3=int(input("enter the integer:"))
if((num1<num2)and (num1<num3)):
    print("num1 is smallest number")
elif((num2<num1)and(num2<num3)):
    print("num2 is smallest number")
else:
    print("num3 is smallest number")