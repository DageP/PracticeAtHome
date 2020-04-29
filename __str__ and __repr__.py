class Person(object):
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self): #__repr__ can return any type of data e.g. string, tuple, dictionaries
        return ("%s %s"%(self.name, self.age))
    #return {"Name":self.name, "age":self.age} will return dictionary-type output

    def __str__(self): #__str__ will always return string-type output
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'

p = Person("Rafi", 17)
print(p.__str__())
print(p.__repr__())
print(type(p.__repr__()))


