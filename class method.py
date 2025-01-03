#class method with out parametor
class mobile:
    @classmethod    # decorator
    def show_model(cls):    #class method
        print("Realme x")
realme=mobile()
mobile.show_model()        #calling clss method
print("---------------------------------------------------")
class mobile1:
    fp='yes'#class variable
    @classmethod
    def show(cls): # class method
    #accessing class variable
        print("fingerprint scanner:",cls.fp)
redmi=mobile1()
mobile1.show()


