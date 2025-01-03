# program to read integer as input and print reversed number of it by using slicing
num=input("enter the integer value:")
list_num=list(num)
print(list_num)
result=''
for i in list_num:
    result=i+result
print(result)
