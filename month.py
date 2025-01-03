month=int(input("enter the month number:"))
#condition to check the month number valid or not
if(month>=1 and month<=12):
    print("valid month number")
else:
    print("invalid month number")
print("-----------------------------------")
num1=int(input("enter the integer:"))
result="valid month number"if(month>=1 and month<=12)else"invalid month number"
print(result)