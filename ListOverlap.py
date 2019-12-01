a = []
b = []
c = []
import random
number = range(1, random.randint(1,150))
number1 = range(1, random.randint(1,500))
for x in number:
    a.append(x)
for x in number1:
    b.append(x)
for x in a:
    if x == x in b:
        if x not in c:
            c.append(x)
print(c)
