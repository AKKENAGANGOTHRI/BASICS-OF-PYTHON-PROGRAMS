#to print number of digits present in given integer
num=int(input("enter the number:"))
digitcount=0
while(num!=0):
    num=num//10
    digitcount=digitcount+1
print(digitcount,"digits")