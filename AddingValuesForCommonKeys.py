d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Final = {}

for key in d1.keys(): #key is for d1
    for key1 in d2.keys(): #x is for d2
        if key == key1:
            b = d1[key] + d2[key1]
            Final[key] = b
        else:
            value = d1[key]
            Final[key] = value
            value2 = d2[key1]
            Final[key1] = value2
print(Final)
