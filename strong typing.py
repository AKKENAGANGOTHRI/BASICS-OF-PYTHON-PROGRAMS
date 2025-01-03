#strong typing
class duck:
    def walk(self):
        print("thapak thapak thapak thapak thapak")
class horse:
    def walk(self):
        print("tabdak tabdak tabtak tabdak tabdak")
class cat:
    def talk(self):
        print("meow meow")
def myfunction(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
d=duck()
myfunction(d)
h=horse()
myfunction(h)
c=cat()
myfunction(c)