num=int(input("enter the integer:"))
rem=0
sum_digits=0
while(num!=0):
    rem=num%10
    sum_digits=sum_digits+rem
    num=num//10
print("sum of digits are",sum_digits)