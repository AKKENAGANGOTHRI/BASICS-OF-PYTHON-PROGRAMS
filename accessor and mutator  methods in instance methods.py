#accessor method or getter method->instance method(1st type)
class markerpen:
    def __init__(self,color,price,brand):
        print("object is created...!")
        self.color=color
        self.price=price
        self.brand=brand
#mutator method or setter method ->instance method (type2)
    def set_color(self):
        self.color='red'
    def set_price(self):
        self.price=25
    def set_brand(self):
        self.brand='doms'
    #Accessor methods
    def show_color(self):
        return self.color
    def show_price(self):
        return self.price
    def show_brand(self):
        return self.brand
m1=markerpen("black",20,"camelin")
res1=m1.show_color()
print(res1)
res2=m1.show_brand()
print(res2)
res3=m1.show_price()
print(res3)
print("========================================")
m2=markerpen("yellow",30,"softek")
res4=m2.show_color()
print(res4)
res5=m2.show_brand()
print(res5)
res6=m2.show_price()
print(res6)
print("==================================")
m1.set_color()
m1.set_price()
m1.set_brand()
res1=m1.show_color()
print(res1)
res2=m1.show_brand()
print(res2)
res3=m1.show_price()
print(res3)

