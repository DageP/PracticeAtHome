import random
number = random.randint(1,9)
guess = input("Guess the number : ")
counter = 0
while guess != 'exit' and guess != number:
    if guess == 'Exit':
        break
    guess = int(input("Guess the number : "))
    if guess < number:
        print("Number is too low")
        counter += 1
    elif guess > number:
        print("Number is too high")
        counter += 1
    else:
        counter += 1
        print("Number is exactly right, it only took you %d tries" %(counter))
    
