#to print the number of alphabets or special characters or digits
str=input("enetr the string:")
str=str.replace(' ','')
alphabet_count=0
special_char_count=0
digit_count=0
for i in str:
    if(i.isalpha()):
        alphabet_count+=1
    elif(i.isdigit()):
        digit_count+=1
    else:
        special_char_count+=1
print("alphabet_count is:",alphabet_count)
print("digit_count is:",digit_count)
print("special_char_count is:",special_char_count)
        
