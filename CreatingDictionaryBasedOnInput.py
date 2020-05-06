Limit = int(input("How many items? "))
Numbers = {}
x = 1
while x <= Limit:
    Numbers[x] = x*x
    x += 1
print(Numbers)
