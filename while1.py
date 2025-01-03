num=int(input("enter the integer value:"))
digitcount=0
#condition to get number of digits
while(num!=0):
    num=num//10
    digitcount=digitcount+1
print(digitcount,"digits")