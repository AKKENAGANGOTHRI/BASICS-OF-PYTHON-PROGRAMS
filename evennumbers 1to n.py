num=int(input("enter the number:"))
print("even numbers from 1 to",num,":")
for i in range(1,num+1):
    if(i%2==0):
        print(i)
        #or
for i in range(2,num+1,2):
    print(i,end=' ')