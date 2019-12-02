number = []
D_Number = int(input("Please enter a number : "))
add = D_Number + 1
x = range(1,add)
divisor = []
for elem in x:
    number.append(elem)
for elem in number:
    if D_Number % elem == 0:
        divisor.append(elem)
for x in divisor:
  print("The factor of %d : %d" %(D_Number, x) )
