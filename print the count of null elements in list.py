#to print the count of null elements in the lust
prog_lang=['c','c++','','java','','python','flutter','','cobalt','','dart','javascript']
print(prog_lang)
null_count=0
for i in prog_lang:
    if(i==''):
        null_count=null_count+1
print("the number of null values are:",null_count)