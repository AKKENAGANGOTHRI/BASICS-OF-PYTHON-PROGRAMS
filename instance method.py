#instance variable with instance class
class mobile:
    def __init__(self):
        self.model="Realme x"
    def show_model(self):
        print(self.model)
realme=mobile()
realme.show_model()
r=realme.model
print("outside class:",r)
        
        