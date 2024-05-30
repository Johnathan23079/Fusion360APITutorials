#fuison360 api
#object = ExtrudeFeature
#Application(Fuison) - UI - Design? - Solid - Extrudefeature
#sketch - sketch line

class LEAD: #name of the class
    #create a function starting with self and two objects, first and second
    def __init__(self, first, second):
        self.first = first #self is at the top of the hierarchy and first is a sub-object
        self.second = second #second is also a sub-object of self
apiSeries = LEAD("first", "second") #this calls 
formsSeries = LEAD("third", "fourth")
print(apiSeries.first)
print(apiSeries.second)


