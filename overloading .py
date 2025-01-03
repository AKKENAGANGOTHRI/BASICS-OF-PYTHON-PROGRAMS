#overloading in polymorphism
class demo:
    def display():
        print("I'm a zero argument method")
    def display(a):
        print("I'm a one  argument method")
    def display(a,b):
        print("I'm a two argument method")
demo.display(2,4)
#overloading in python is not existing