#example dictionary
dict={101:'python',201:'java',301:'c',401:'c++'}
print(dict)
print(type(dict))
print("--------------------------------------------------")
print(dict[101])
print(dict[201])
print(dict[301])
print(dict[401])
dict[501]='sql'
print("-------------------------------------------------------")
print(dict)
dict[101]='flutter'
print("----------------------------------------------------")
print(dict)
print()
del dict[301]
print(dict)
print()
new_dict=dict.copy()
print(new_dict)
dict.update({105:'css',205:'html'})
print(dict)
nested_dict={'dict1':{'name1':'gangu'},'dict2':{'name2':'krishna'}}
print(nested_dict)