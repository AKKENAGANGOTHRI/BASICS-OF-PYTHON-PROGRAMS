#example of functions
def display():
    print('python')
    print('java')
    print('html')
    print('c++')
    print('flutter')
display()
display()
display()
print("=======================================================================")
#function inside the multiple function

def eat():
    print("eat food")
def washhands():
    print("wash your hands")
    def servefood():
        print("serve food")
    eat()
    print("wash your hands")
washhands()

