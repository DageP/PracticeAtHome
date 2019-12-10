sentence = str(input("Please enter a sentence :"))
a = sentence.split()
if len(a) <= 1:
    print("ENTER A SENTENCE!")
    exit()
elif len(a) > 1:
    print(a[::-1]) #Reverse the order of a list or characters


