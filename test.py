print ("1333")
class tekla:
    def __init__(self):
        self.x=21
        self.y=22
    def move(self):
        self.x+=1

class tekka_sub(tekla):
    def __init__(self):
        super().__init__()

a=tekla()
p=a.move()
print(p)
print (a.x)

b=tekka_sub()
#b.x=33
b.move()
print ("class bb=",b.x)

class deleter:
    def __init__(self):
        self.x=100
    def start(self):
        self.x+=1
        print (f"x={self.x}")
        if self.x<=124:
           self.start()

a=deleter()
a.start()





