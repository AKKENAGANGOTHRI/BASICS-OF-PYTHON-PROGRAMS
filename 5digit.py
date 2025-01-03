num=int(input("enter the integer:"))
#condition to check the integer is five digit or not
if((num>=10000 and num<=99999) or (num>=-99999 and num<=-10000)):
    print("five digit number")
else:
    print("not a five digit number")
print("--------------------------------")
num1=int(input("enter the integer:"))
result="five digit number"if((num>=10000 and num<=99999) or (num>=-99999 and num<=-10000))else "not a five digit number"
print(result)