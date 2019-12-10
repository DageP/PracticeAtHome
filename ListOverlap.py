c = []
import random
# random.sample --> Prints list of random items of given length
# Using randrange() to generate a number from 0-100
number = random.sample(range(1, random.randrange(150)), random.randint(1,10))
number1 = random.sample(range(1, random.randrange(500)), random.randint(1,10))
a = [x for x in number]
b = [x for x in number1]
print(a)
print(b)
for x in a:
    if x == x in b:
        if x not in c:
            c.append(x)
print(c)
