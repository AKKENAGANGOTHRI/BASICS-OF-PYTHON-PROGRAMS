num1=int(input("enter the integer:"))
num2=int(input("enter the integer:"))
if(num1<num2):
    print("num1 is smallest number")
elif(num1==num2):
    print("num1 is equal to num2")
else:
    print("num2 is smallest number")
print("------------------------------------------------")
num1=int(input("enter the integer:"))
num2=int(input("enter the integer:"))
result1="num1 is smallest"if(num1>num2)else"num2 is smallest"
print(result1)