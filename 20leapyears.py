#to print 20 leap years to given integer
year=int(input("enter the year:"))
count=20
leapcount=0
print("leap years:")
while(leapcount!=count):
    if((year%4==0 and year%100!=0) or year%400==0):
        leapcount+=1
        print(year)
    year+=1

    