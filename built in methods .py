#examples for methods in python
cartoons=['little krishna','tom & jerry','krishna aur balaram','dora','chota bheem','ben-ten']
print("after appending the  element:")
cartoons.append('shichan')
print(cartoons)
print("after inserting the  element:")
cartoons.insert(2,'motu-pathulu')
print(cartoons)
print("after poppinf the  element:")
cartoons.pop(4)
print(cartoons)
print("after removing the  element:")
cartoons.remove('chota bheem')
print(cartoons)
print(cartoons.index("tom & jerry"))
print("after reversing the  element:")
cartoons.reverse()
print(cartoons)
#extend
a=[2,4,6,8,10]
b=[1,3,5,7,9]
print(a)
a.extend(b)
print(a)
b.extend(a)
print(b)
#count
acount=a.count(10)
bcount=b.count(9)
print(acount)
print(bcount)
#sort
n=[1,5,3,7,3,8,2,9]
n.sort()
print(n)