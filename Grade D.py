import random # Importing random libary - which allows the code to randomise values


# Defining variables for cards in a deck
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')


# Defining the number of cards being used
NCARDS = 8


# Creating the function which simulates drawing a random card from a deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pops one off the top of the deck and returns it
    return thisCard


# Makes a copy of the starting deck and randomly shuffles it   
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut


# Shows texts in 2 separate lines, in the terminal (spits it out, if that makes sense)
print('Welcome to the Game')
print('The programmer has forgotten to give you the game instructions.')

# Instructions (also found at bottom of file)
# Creates a empty list to store random card values, it then defines each card (52 cards) with a value
# based on their number, also stores the suit. This nested loop keeps repeating itself until
# every card in a pack is defined and stored in the list

startingDeckList = []
# Goes through giving each card a value for each of the 4 suits (until they have all the been defined)
for suit in SUIT_TUPLE:
    # Iterates through each rank making it in a dictionary
    for thisValue, rank in enumerate(RANK_TUPLE):
        # Assignes each card a order to store its composition (differently for each xard)
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        # Each card's dictionary is added to the starting deck list 
        startingDeckList.append(cardDict)


# Gives score a value (which will eventually be changed, it's a starting point for the user)     
score = 50




while True:
    # the 'print()' is used to create a blank line for readability, it is used numerous times below
    print()
    # the deck that will be used in the game is shuffled from the starting order 
    gameDeckList = shuffle(startingDeckList)
    # It gets the first cards information stored in the dictionary
    currentCardDict = getCard(gameDeckList)
    # It gets the ranks (number on the card) of the card from the dictionary
    currentCardRank = currentCardDict['rank']
    # It gets the number in the deck which the card is
    currentCardValue = currentCardDict['value']
    # It gets the suit of the card
    currentCardSuit = currentCardDict['suit'] 
    # It calls the number of the card and the suit of the card and prints it   
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()


    for cardNumber in range(0, NCARDS):   # play one game of this many cards
        # The user is asked to input their answer to the question (higher or lower?) and 
        # their answer is stored and assigned to the 'answer' variable
        answer = input('Will the next card be higher or lower than the ' + 
                               currentCardRank + ' of ' + 
                               currentCardSuit + '?  (enter h or l): ')
        answer = answer.casefold()  # forces lower case of their answer
        # The next card in the game deck list is called and assigned to the next card value
        nextCardDict = getCard(gameDeckList)
        # The rank, value and suit of the next card is assigned to a value from the card dictionary
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        # Prints the rank and suit of the next card into the terminal
        print('Next card is:', nextCardRank + ' of ' + nextCardSuit)

        # FOLLOWING COMMENTS ARE FOR LINES 81 - 96:
        # If they answered higher and got it correct their score will update to add 20 (and display correct text in terminal)
        # if they still answered higher but got it wrong, their score will minus 15 (and display incorrect text in terminal)
        # Same for lower input, their scores will update if they are correct or not (as well as correct or incorrect messages)
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15          

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        # After their score has been totalled it their updated score will display in the terminal
        print('Your score is:', score)
        print()
        # The 'next card' values are now ressasigned as the current card (for when rounds are repeated)
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
        currentCardSuit = nextCardSuit

    # if user wants to play again and press's ENTER the game restarts, if the user 
    # enters 'q' the game ends
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break


# Prints 'OK bye' in the terminal, ending the game
print('OK bye')



# RULES OF THE GAME:

# Gameplay: Each round the user needs to guess whether or not the next card is 
# higher or lower than the previous card

# Scoring: The player starts with 50 points, if a player is correct they recieve 20
# points, but if incorrect the lose 15

# Rules: Please enter only "h" or "l" to indicate your play, the game ends once the
# 8 rounds have finished. 

# Have fun and good luck!
