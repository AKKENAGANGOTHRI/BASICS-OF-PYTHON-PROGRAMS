#instance method with parameter
class mobile:
    def __init__(self):
        print("object is created....!")
        self.price=15000
    def show_price(self,price):
        print(self.price)
samsung=mobile()
samsung.show_price(1000)    