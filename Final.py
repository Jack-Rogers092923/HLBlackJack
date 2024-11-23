import html
import random
# Ask the user what game they would like to play
GameSelection = int(input("What game would you like to play| 1. Higher or Lower | 2. Black Jack |\n"))
playerSum = 0
dealerSum = 0
playercardsvalue = []
playercardsword = []
dealercardsvalue = []
dealercardsword = []
ht=0


#region Player Def
def DrawCard():
    card = random.randint(2,14) 
    if card == 14 or card==13 or card==12:
        card=10   
    return card

def CardWord(card):
    if card == 14:
        cardword="Jack"
    elif card==12:
        cardword="Queen"
    elif card==13:
        cardword="King"
    elif card==11:
        cardword="Ace"
    else:
        cardword=str(card)
    return cardword


def PrintCurrentHand():
    hand = ""
    for i in playercardsword:
        hand += i + ", "
        
    return hand


def HandTotal():
    global ht
    ht = 0
    for i in playercardsvalue:
        ht+=i
    return ht
#endregion
#region Dealer Def
def DrawCard():
    card = random.randint(2,14) 
    if card == 14 or card==13 or card==12:
        card=10   
    return card

def CardWord(card):
    if card == 14:
        cardword="Jack"
    elif card==12:
        cardword="Queen"
    elif card==13:
        cardword="King"
    elif card==11:
        cardword="Ace"
    else:
        cardword=str(card)
    return cardword


def PrintCurrentHand2():
    hand = ""
    for i in dealercardsword:
        hand += i + ", "
        
    return hand


def HandTotal2():
    global ht
    ht = 0
    for i in dealercardsvalue:
        ht+=i
    return ht
#endregion

# If the user chose higher or lower run all of this mess
# region Higher or Lower
if GameSelection == 1:
    cBet = 10
    print("You have chosen to play Higher or Lower")
    print("Your Starting Balance is $10")
    # If the balance is still above 0 keep playing
    while cBet > 0:
        bet = int(input("What would you like your bet to be: "))
        # If their bet is more than they have, don't run
        if(bet>cBet):
            print("You do not have enough money for this bet")
            break;
        # Randomize the two cards 
        hl = random.randint(2,14)
        hl2 = random.randint(2,14)
        # If 11 then the card displays Jack
        if hl == 11:
            print("The Card is: Jack")
        # If 12 then the card displays Queen
        elif hl == 12:
            print("The Card is: Queen")
        # If 13 then the card displays King
        elif hl == 13:
            print("The Card is: King")
        # If 14 then the card displays Ace
        elif hl == 14:
            print("The Card is: Ace")
        else: print("The Card is:", hl)
        higherlower = int(input("Would you like to take the higher or lower? | 1. Higher | 2. Lower |\n"))
        if higherlower == 1 and hl < hl2:
            cBet += bet
            print("You won $"+ str(bet))
            print("Your Current Balance is: $"+ str(cBet))
        if higherlower == 1 and hl > hl2:
            cBet -= bet
            print("You lost $"+ str(bet))
            print("Your Current Balance is: $"+ str(cBet))    
        if higherlower == 2 and hl < hl2:
            cBet -= bet
            print("You lost $"+ str(bet))
            print("Your Current Balance is: $"+ str(cBet))
        if higherlower == 2 and hl > hl2:
            cBet += bet
            print("You won $"+ str(bet))
            print("Your Current Balance is: $"+ str(cBet))
        if hl2 == 11:
            print("The Card was a: Jack")
        elif hl2 == 12:
            print("The Card was a: Queen")
        elif hl2 == 13:
            print("The Card was a: King")
        elif hl2 == 14:
            print("The Card was a: Ace")
        else: print("The Card was:", hl2)   
        if higherlower == 1 and hl == hl2:
            print("The Card was the same your bet has been returned")
        if higherlower == 2 and hl == hl2:
            print("The Card was the same your bet has been returned")
#endregion
# If user choses Black Jack run all of this mess
# region Black Jack
if GameSelection == 2:
    cBet = 10
    playerSum = 0
    print("You have chosen to play Black Jack")
    print("Aces are only used as 11")
    print("Your Starting Balance is $10")
    while cBet > 0:
        # Reset player's sum to 0 at the beginning of each game
        playerSum = 0  
        playercardsvalue = []
        playercardsword = []

        # Reset Dealer's sum to 0 at the beginning of each game
        dealerSum = 0  
        dealercardsvalue = []
        dealercardsword = []

        # Ask player what they want to bet
        bet = int(input("What would you like your bet to be: "))
        
        # If the player's bet is larger than what they have end game
        if(bet>cBet):
            print("You do not have enough money for this bet")
            break
        # region Players Cards

        # Draw players first card
        c = int(DrawCard())
        playercardsvalue.append(c)
        cw = CardWord(c)
        playercardsword.append(cw)

        # Draw second card
        c = DrawCard()
        playercardsvalue.append(c)
        cw = CardWord(c)
        playercardsword.append(cw)

        # Get current total
        playerSum=HandTotal()
        #endregion



        #region Dealers Cards
        # Draw dealers first card
        c = int(DrawCard())
        dealercardsvalue.append(c)
        cw = CardWord(c)
        dealercardsword.append(cw)

        # Draw second card
        c = DrawCard()
        dealercardsvalue.append(c)
        cw = CardWord(c)
        dealercardsword.append(cw)

        # Get current total
        dealerSum=HandTotal2()
        #endregion
        
        # Show what cards the dealer has 
        print("===================")
        print("The Dealers Cards are:", PrintCurrentHand2())
        print(f"Dealers Total: {dealerSum}")
        print("===================")
        # Show what cards the player has 
        print("The Players Cards are:", PrintCurrentHand())
        print(f"Players Total: {playerSum}")
        print("===================")
        
        while dealerSum <=16:
            # Reset player sum
            dealerSum = 0

            # Draw next card
            card = DrawCard()
            dealercardsvalue.append(card)
            cw = CardWord(card)
            dealercardsword.append(cw)

            # Get current total
            dealerSum=HandTotal2()
            print("The Dealer has Hit")

            # Show what cards the dealer has 
            print("The Dealers Cards are:", PrintCurrentHand2())
            print(f"Dealers Total: {dealerSum}")
            print("===================")

        # While players sum is less than or equal to 21 run all of this
        while playerSum <= 21:
            if(dealerSum > 21):
                cBet += bet
                print(f"Dealer Bust \nYou Won ${bet}")
                print(f"Your current balance is ${cBet}")
                break
            # Ask the user if they want to hit or stand
            hs = int(input("What would you like to do? | 1. Hit | 2. Stand |\n"))
            # If user hits randomize new number to add to their total sum 
            if hs == 1:
                # Reset player sum
                playerSum = 0

                # Draw next card
                card = DrawCard()
                playercardsvalue.append(card)
                cw = CardWord(card)
                playercardsword.append(cw)

                # Get current total
                playerSum=HandTotal()

                # Show what cards the Dealer has 
                print("The Dealers Cards are:", PrintCurrentHand2())
                print(f"Dealers Total: {dealerSum}")

                # Show what cards the Player has 
                print("The Player Cards are:", PrintCurrentHand())
                print(f"Players Total: {playerSum}")
               
            elif hs == 2:
                # If the player sum is less than or = to 21 and larger than the dealer sum they win
                print(f"You have chosen to stand with {playerSum}")
                if(playerSum <= 21 and playerSum > dealerSum):
                    cBet += bet
                    print(f"You Won ${bet}")
                    print(f"Your current balance is ${cBet}")

                # If player sum is less than dealer sum they lose
                if(playerSum < dealerSum):
                    cBet -= bet
                    print(f"Dealer wins \nYou lost ${bet}")
                    print(f"Your current balance is ${cBet}")

                # If player sum and dealer sum are the same return the bet
                if(playerSum == dealerSum):
                    print("Push \n" "Your bet has been returned")
                    print(f"Your current balance is ${cBet}")
                break

        # If player sum is larger than 21 player busts    
        if(playerSum > 21):
            cBet -= bet
            print(f"Player Bust \nYou lost ${bet}")
            print(f"Your current balance is ${cBet}") 
            
#endregion