# sum 
def add(y):
    x=10
    c=x+y
    return c
sum=add(20)
print(sum)
print()
#nested functions
def disp():
    def show():
        print("show function")
    print("display function")
    show()
disp()
print()
