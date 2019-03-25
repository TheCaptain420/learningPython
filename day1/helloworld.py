print ("Hello world")

#method
def printHello(fname):
    print ("hello "+fname)

printHello("Mads")

#Object/class
class Person():
    age = "21"
    def __init__(self, sname, describ):
        self.name = sname; 
        self.describ = describ; 
    
    def getName(self):
        return self.name
    
    def getDisc(self):
        return self.describ

def printAPerson(tObject):
    print ("hello "+  tObject.getName()+" you are "+ tObject.getDisc());



person1 = Person("Jay","A Person"); 
person2 = Person("Heinz", "also a person")
print ("hello "+  person1.getName()+" you are "+ person1.getDisc());
printAPerson(person2); 
print (person1.age) 
