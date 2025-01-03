#declaring lambda function
result=lambda num:print(num)#single argument
result(100)
print("-------------------------")
res=lambda a,b:print(a*b)#two arguments
res(45,2)
print("----------------------------")
add_sub=lambda x,y:(x+y,x-y)#return multiple
a,s=add_sub(6,3)
print(a)
print(s)
print("-----------------------")
#condition to check whether the number is even or not
even=lambda x:print("even") if x %2==0 else print("not even")
even(5)
print("-----------------------")
#is digit or unumber
integer=lambda a:print("digit")if a>=-9 and a<=9 else print("number")
integer(45)
print("=====================")
n=lambda x:print("two digit") if (x>=-10 and x<=-99) or (x>=10 and x<=99) else print("not a two digit")
n(334)
n1=lambda x:print("three digit") if(x>=-100 and x<=-999) or (x>=100 and x<=999) else print("not a three digit")
n1(234)
n2=lambda x:print("four digit") if(x>=-1000 and x<=-9999) or (x>=1000 and x<=9999) else print("not a four digit")
n2(2345)
n3=lambda x:print("four digit") if(x>=-10000 and x<=-99999) or (x>=10000 and x<=99999) else print("not a four digit")
n3(4235)