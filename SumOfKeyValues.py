Number = {"First" : 1, "Second" : 2, "Third" : 3}
Sum = 0
for x in Number:
    Sum = Sum + Number[x]
print(Sum)

#print(sum(Number.values())) can be used for efficiency
