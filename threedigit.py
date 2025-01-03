num=int(input("enter the integer:"))
#condition to check the integer is three digit or not
if((num>=100 and num<=999)or(num>=-999 and num<=-100)):
    print("three digit number")
else:
    print("not a three digit number")
print("--------------------------------")
num1=int(input("enter the integer:"))
result="three digit number"if((num>=100 and num<=999)or(num>=-999 and num<=-100))else "not a two digit number"
print(result)