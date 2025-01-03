# python program to print the number of alphabets ,special characters and digits in the string
str=input("enter the string:")
str=str.lower()
str=str.replace(' ','')
alpha_count=0
special_count=0
digit_count=0
for i in str:
    if i.isalpha():
        alpha_count+=1
    elif i.isdigit():
        digit_count+=1
    else:
        special_count+=1
print("alpha_count is:",alpha_count)
print("digit_count is:",digit_count)
print("special_count is:",special_count)