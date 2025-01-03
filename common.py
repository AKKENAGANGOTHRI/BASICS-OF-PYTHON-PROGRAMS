def CommonDigits(a,b,c):
    a_set=set(str(a))
    b_set=set(str(b))
    c_set=set(str(c))
    CommonDigits=a_set & b_set & c_set
    return sorted(CommonDigits)
a=int(input())
b=int(input())
c=int(input())
result=CommonDigits(a,b,c)
print(result)