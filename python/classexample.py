import datetime #datetime module for born year method
class Student: #declare class
    name = ''
    age = 0
    classin = '' #private attributes
    id = 0
    phonenum = 0
    def __init__(self, n, a, cin, i, pn):
        self.name = n
        self.age = a
        self.classin = cin # constructor with init
        self.id = i
        self.phonenum = pn
    def calcbornyear(self):
        age = self.age
        nowyear = datetime.date.today().year # calc year that is born from age and now year
        bornyear = nowyear - age
        return bornyear
    def returnattrib(self):
        return [self.name,self.age,self.classin,self.id,self.phonenum] # return attributes as list

name = Student('Name Here', 17, 'Class99',1,98899989) # new object
print(name.calcbornyear()) # call methods
print(name.returnattrib())
