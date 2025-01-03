age=int(input("enter the age:"))
#condition to check the age is eligible to vote or not
if(age>=18):
    print("eligible to vote....!")
else:
    print("not eligible to vote...!")
print("---------------------------------------")
num1=int(input("enter the age:"))
result="eligible to vote...!"if(num1>=18) else "not eligible to vote....!" 
print(result)