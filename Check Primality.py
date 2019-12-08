D_Number = int(input("Please enter a number : "))
def prime_num():
    add = D_Number + 1
    x = range(1,add)
    divisor = []
    number = [elem for elem in x]
    for elem in number:
        if D_Number % elem == 0:
            divisor.append(elem)
    print(divisor)
    factors = len(divisor)
    if factors <= 2:
        print(D_Number, "is a prime number")
    else:
        print(D_Number, "is not a prime number")
    
prime_num()



