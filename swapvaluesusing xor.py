a=int(input("enter a: "))
b=int(input("enter b: "))
#swapping two integer values using xor operator
print("value of a,b before swapping:",(a,b))
a=a^b
b=a^b
a=a^b
print("values of a,b after swapping:",(a,b))