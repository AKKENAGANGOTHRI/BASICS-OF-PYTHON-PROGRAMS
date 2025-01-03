str=input("enter the string:")
vowel_count=0
for i in str:
    if(i in ('A','E','I','O','U','a','e','i','o','u')):
        vowel_count+=1
print("vowel count is:",vowel_count)
print("------------------------------------------------")
str2=input("enter the string:")
vowel_count1=0
consonent_count=0
for i in str2:
    if(i in ('A','E','I','O','U','a','e','i','o','u')):
        vowel_count1+=1
    else:
        consonent_count+=1
print("vowel count is",vowel_count1)
print("consonent count is",consonent_count)
print("------------------------------------------")
str2=input("enter the string:")
vowel_count2=0
consonent_count2=0
str=str.lower()
str=str.replace(' ','')
for i in str:
    if(i in ('a','e','i','o','u')):
        vowel_count2+=1
    elif(i.isalpha()):
        consonent_count2+=1
print("vowel count is:",vowel_count2)
print("consonent count is",consonent_count2)