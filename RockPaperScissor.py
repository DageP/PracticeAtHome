Op1 = "Rock" 
Op2 = "Paper"
Op3 = "Scissor"
Elements = ['Rock','Paper','Scissor','No']

def game():
    print("Write either 'Rock', 'Paper' or 'Scissor'")
    Player1 = str(input("Enter your item : "))
    Player2 = str(input("Enter your item : "))
    if Player1 and Player2 in Elements:
        while Player1 or Player2 != "No":
            if Player1 == Player2:
                print("It's a draw")
                break
            if Player1 == Op1:
                if Player2 == Op2:
                    print("Player2 wins")
                    break
                else:
                    print("Player1 wins")
                    break
            if Player1 == Op2:
                if Player2 == Op3:
                    print("Player2 wins")
                    break
                else:
                    print("Player1 wins")
                    break
            if Player1 == Op3:
                if Player2 == Op1:
                    print("Player2 wins")
                    break
                else:
                    print("Player1 wins")
                    break
    else:
        print("Inputs are wrong")
        game()
game()

