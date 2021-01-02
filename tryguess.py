#Start
def start():
    print ("Hello dude! - Nmbrthirteen\n")
    print ("Your goal is to guess number, which i have in my mind \n")
    print ("also, you have only 10 attempts")
    print ("\nNumber is from 1 to 50")
    try:
        firstQuestion = input("Can we start?(yes or no): ")
        if firstQuestion == "yes" or firstQuestion == "Yes":
            trytoGuess();
        else:
            print("Okay, I can only say goodbye now :/")
    except:
        print("Okay, I can only say goodbye now ://")
#Restart
def start2():
    print ("\nHello again dude! - Nmbrthirteen")
    print ("\nYou know but - Your goal is to guess number, which i have in my mind \n")
    print ("also, you have only 10 attempts")
    print ("\nNumber is from 1 to 50")
    try:
        trytoGuess();
    except:
        print("Okay, I can only say goodbye now ://")
    
def trytoGuess():
    #Number to guess
    import random
    toGuess = random.randrange(1,50)
    tryGuess = ''
    #Tries
    tries = 0
    while toGuess != tryGuess and tries != 10:
        tries += 1
        tryGuess = int(input("Guess it: "))
        #Higher and Lower
        if toGuess > tryGuess:
            print("\nMy Number is higher than your guess")
        elif tryGuess == "exit":
            break
        elif toGuess < tryGuess:
            print("\nMy Number is lower than your guess")
        ##Tries
        if tries == 10:
            print("\nYou have run out of attempts")
            lastQuestionisa = input("Do you need to play again?(yes or no): ")
            if lastQuestionisa == "yes" or lastQuestionisa == "Yes" or lastQuestionisa == "YES":
                start2();
            else:
                print("\nOkay, Goodbye - Thanks for Playing!")
        #Correct Answer
        if toGuess == tryGuess:
            print("Oh my god! you guessed it!!" or "Bravo! you guessed it!")
            lastQuestion = input("Do you need to play again?(yes or no): ")
            if lastQuestion == "yes" or lastQuestion == "Yes" or lastQuestion == "YES":
                start2();
            else:
                print("\nOkay, Goodbye - Thanks for Playing!")
                break
            
start()