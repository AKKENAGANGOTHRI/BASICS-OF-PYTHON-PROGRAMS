#to print number of odd digits present in given integer
num=int(input("enter the number:"))
odddigitcount=0
rem=0
while(num!=0):
    rem=num%10
    if(rem%2!=0):
        odddigitcount=odddigitcount+1
    num=num//10
print("number of odd digits are",odddigitcount)