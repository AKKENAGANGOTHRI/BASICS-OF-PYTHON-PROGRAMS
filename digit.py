num=int(input("enter the integer:"))
#condition to check the integer is digit or not
if((num>=-9 and num<=9)):
    print("digit")
else:
    print("number")
print("------------------------------------------")
num1=int(input("enter the integer:"))
result="digit" if((num1>=-9 and num1<=9)) else"number"
print(result)