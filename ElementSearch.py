import random

check = False
d_number = random.sample(range(1, random.randrange(50)), random.randint(1,20))
number = [x for x in d_number]
number.sort()
random_num = random.randrange(50)
for x in number:
    if x == random_num:
        check = True
        print(check)
        print("The number :", random_num, "is on the list")
        break
if x != random_num:
    print("The number is not inside the list")

