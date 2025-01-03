num=int(input("enter the value of num:"))
#even numbers
print("even numbers from 1 to",num,":")
list(map(lambda i:print(i,),range(2,num+1,2)))
print()
#odd numbers
print("odd numbers from 1 to",num,":")
list(map(lambda i:print(i,),range(1,num+1,2)))
