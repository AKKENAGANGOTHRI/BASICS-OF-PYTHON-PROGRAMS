#duck typing(example 1)
class duck:
    def walk(self):
        print("thapak thapak thapak thapak thapak")
class horse:
    def walk(self):
        print("tabdak tabdak tabtak tabdak tabdak")
def myfunction(obj):
        obj.walk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)
print()
#example 2
class father:
    def work(self):
        print("hard working father...!")
class son:
    def work(self):
        print("enjoying son....!")
def result(self):
    self.work()
f1=father()
f1.work()
s1=son()
s1.work()