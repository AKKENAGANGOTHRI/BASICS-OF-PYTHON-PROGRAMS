num=int(input("enter the integer:"))
#condition to check the integer is two digit or not
if((num>=10 and num<=99) or (num>=-99 and num<=-10)):
    print("two digit number")
else:
    print("not a two digit number")
print("--------------------------------")
num1=int(input("enter the integer:"))
result="two digit number"if((num>=10 and num<=99) or (num>=-99 and num<=-10))else "not a two digit number"
print(result)