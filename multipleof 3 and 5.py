num=int(input("enter the integer:"))
#condition to check the integer is multipled by both 3 and 5
if(num%3==0 and num%5==0):
    print("multiplied by both 3 and 5")
else:
    print("not multipled by both 3 and 5")
print("----------------------------------------")
num1=int(input("enter the integer:"))
result="multiplied by both 3 and 5" if(num1%3==0 and num1%5==0)else"not multiplied by 3 and 5"
print(result)