class dictObj(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def createDict(self):
        a = {}
        a["x"] = self.x
        a["y"] = self.y
        a["z"] = self.z
        return a

Dict = dictObj("Red", "Yellow", "Blue")
print(Dict.createDict())       
        
# More code efficient way
class dictObj(object):
     def __init__(self):
         self.x = 'red'
         self.y = 'Yellow'
         self.z = 'Green'
     
test = dictObj()
print(test.__dict__)
