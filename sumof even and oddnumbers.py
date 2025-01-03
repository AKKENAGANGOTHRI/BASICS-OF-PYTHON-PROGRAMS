#to print the sum of even and odd numbers  from 1 to n
num=int(input("enter the number:"))
evensum=0
oddsum=0
for i in range(1,num+1):
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i
print("even sum :",evensum)
print("odd sum:",oddsum)