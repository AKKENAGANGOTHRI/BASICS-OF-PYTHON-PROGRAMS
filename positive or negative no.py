num=int(input("enter the integer:"))
#condition to check the number is positive or negative or zero
if(num>0):
    print("positive number")
elif(num==0):
    print("zero")
else:
    print("negative number")
print("----------------------------------")
num1=int(input("enter the integer:"))
result1="positive number" if(num1>0) else "zero"
print(result1)
result2="negative number"if(num1<0) else "zero"
print(result2)