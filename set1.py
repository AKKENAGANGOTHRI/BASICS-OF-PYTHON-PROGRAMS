set={'black','red','green','blue','yellow','orange'}
print(set)
print(type(set))
print("=============================================")
print("adding one element")
set.add('purple')
print(set)
set.add('violet')
print(set)
set.add('light green')
print(set)
set1={'lavender','indigo','rosegold','peach','pink'}
set.update(set1)
print("--------------------------------------------")
print("adding multiple elements of set")
print(set)
print("=============================================================")
print("deleting element of set")
set.remove('pink')
print(set)