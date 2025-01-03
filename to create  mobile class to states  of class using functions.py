class mobile:
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
def mobile_details(self):
    print("mobile brand:",self.brand)
    print("mobile color:",self.color)
    print("mobile price:",self.price)
mobile1=mobile("vivo","orange",15000)
mobile2=mobile("redmi","blue",20000)
mobile3=mobile("realmi"," violet",30000)        
mobile_details(mobile2)
print("=======================================")
mobile_details(mobile1)
print("=======================================")
mobile_details(mobile3)