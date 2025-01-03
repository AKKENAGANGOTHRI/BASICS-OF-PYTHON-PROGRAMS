#method overloading
class Engineer:
    def work(self):
        print("Engineer is working...!")
class SoftwareEngineer(Engineer):
    def work(self):
        print("software engineer  is working .....!")
class ElectricalEngineer(Engineer):
    def work(self):
        print("Electrical  engineer  is working .....!")
E1=Engineer()
E1.work()
S1=SoftwareEngineer()
S1.work()
Ee1=ElectricalEngineer()
Ee1.work()