# to print odd numbers from 1 to n
num=int(input("enter the number:"))
print("odd numbers from 1 to",num,":")
for i in range(1,num+1):
    if(i%2!=0):
        print(i)