num=int(input("enter the integer:"))
#condition to check the integer is four digit or not
if((num>=1000 and num<=9999) or (num>=-9999 and num<=-1000)):
    print("four digit number")
else:
    print("not a four digit number")
print("--------------------------------")
num1=int(input("enter the integer:"))
result="four digit number" if((num>=1000 and num<=9999) or (num>=-9999 and num<=-1000))else "not a four digit number"
print(result)