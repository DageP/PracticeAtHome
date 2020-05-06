import operator #This is a module for arithmetical operations
Songs = {
  "Aubrey" = 1
  "Blue Sky Collapse" = 3
  "September" = 5
  "Midnight" = 4
  "Tokyo Light" = 2
}
Sorted = dict(sorted(Songs.items(), key=operator.itemgetter(0))) #The key of dictionary (the first element, hence 0) is set as the operator
print(Sorted) #itemgetter() is a function to retrieve an item
#To sort a dictionary item values --> dict(sorted(Songs.items(), key=operator.itemgetter(1)))
