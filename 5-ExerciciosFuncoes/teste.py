import random

dado = 0

def craps(dado):
    dado = random.randrange(2, 13)
    if dado == 7 or dado == 11:
        print("You are 'The incredible' and won, your number: ", dado)
    elif dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dado == 10:
        print("You are in your point, this is your number: ", dado)

        ponto = 0
        while ponto != dado:
            inp = input("Press ENTER to proceed: ")
            if inp == "":
                ponto = random.randrange(2,13)
                print("Your number is: " , ponto)
                if ponto == 7:
                    print("You losed")
                    break
    else:
        print("Craps, you losed!")

craps(dado)