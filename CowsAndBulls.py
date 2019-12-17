def validation():
    if e_number < 1000 or e_number > 9999:
        print("The quantity of number entered is invalid")
        exit()

    

import random

r_number = random.randrange(1000,9999)
e_number = int(input("Please enter a 4-digit number : "))
validation()
Cow = 0
Bull = 0
while 1:
    if e_number == r_number:
        Cow += 1
        print("Cows : ", Cow)
        print("Bulls : ", Bull)
        e_number = int(input("Please enter a 4-digit number : "))
        validation()
    elif e_number != r_number:
        Bull += 1
        print("Cows : ", Cow)
        print("Bulls : ", Bull)
        e_number = int(input("Please enter a 4-digit number : "))
        validation()
    elif e_number == 0:
        exit()
        
