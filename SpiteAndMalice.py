# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Spite and Malice Classes:
# 1. Card Class
# 2. Play Stack Class
# 3. The Hand Class

import random


class CardClass():
    '''
    A class for all types of cards for use in the game
    Inputs: value: 0 - 9, and -1 for jokers
    Returns: None
    '''

    def __init__(self, value):

        assert (value >= -1 and value <= 9), "error value not in range"
        self.__value = value
        if value == -1:
            self.__face = '*'
        else:
            self.__face = str(value)

    def assign(self, value):
        '''
        Assigns value to each card
        Inputs: value
        Outputs: none
        '''
        if self.__face == '*':
            self.__value = value

    def getValue(self):
        '''
        Returns the value of a card
        Inputs: none
        Outputs: none
        '''
        return self.__value

    def getFace(self):
        '''
        Returns the face of a card
        Inputs: none
        Outputs: none
        '''
        return str(self.__face)

    def __str__(self):
        '''
        String conversion function
        Inputs: none
        Outputs: face
        '''
        return str(self.__face)

    def __repr__(self):
        '''
        String representation function
        Inputs: none
        Outputs: card face with value
        '''
        # return str(self.__face) + "." + self.__value
        return self.__face


class PlayStack():
    '''
    Initializes a play Stack for the centre of the table
    Inputs: none
    Outputs: none
    '''

    def __init__(self):
        self.__cards = []

    def getCard(self):
        '''
        Pops the top card on the stack
        Inputs: none
        Outputs: card object from top of stack of type CardClass
        '''
        return self.__cards.pop()

    def peekValue(self):
        '''
        Gives the value of the top card of stack; raises error if no cards in stack
        Inputs: none
        Outputs: value of card on top of stack
        '''
        if len(self.__cards) == 0:
            raise Exception("Error: No cards in the playing stack")
        else:
            return self.__cards[len(self.__cards) - 1].getValue()

    def peekFace(self):
        '''
        Gives face of card on top of stack; raises error if no cards in stack
        Inputs: none
        Outputs: face of card on top of stack
        '''
        if len(self.__cards) == 0:
            raise Exception("Error: No cards in the playing stack")
        else:
            return '[%s]' % self.__cards[len(self.__cards) - 1].getFace()

    def playCard(self, card):
        '''
        Main method of the game: this method receives cards into a play stack;
        raises exception if card is an illegal play: 1. empty stacks can only receive 0 or jokers; 2. If stack is not empty
        can only recieve card of value one higher than top card, or can receive a joker.
        Inputs: card object of type CardClass
        Outputs: none
        '''
        if self.__cards == []:  # If list is empty can receive a zero, or a '*'
            if (card.getValue() > 0):
                raise Exception("Error: Card rejected; Please make another choice.")
            if (card.getValue() == 0 or card.getValue() == -1):
                self.__cards.append(card)
            if card.getValue() == -1:
                card.assign(0)  # Assigns value of zero to '*' card

        else:
            if self.__cards is not []:  # If list is not empty, can receive next higher card, or a '*'
                if (card.getValue() == self.__cards[(len(self.__cards)) - 1].getValue() + 1):
                    self.__cards.append(card)
                if card.getValue() == -1:
                    card.assign(self.__cards[(
                                                 len(self.__cards)) - 1].getValue() + 1)  # Assigns value of previous + 1 to '*' card
                    self.__cards.append(card)

    # def length(self):
    # return len(self.__cards)

    def __str__(self):
        '''
        String representation function
        Inputs: none
        Outputs: String representation of format: '|[][][]|'
        '''
        string = '|'
        for item in self.__cards:
            string += '[' + item.getFace() + ']'
        return string + '|'


class Hand():
    '''
    Class for the players' hands; holds five cards max of type CardClass; raises error if more than five cards added
    Inputs: none
    Outputs: none
    '''

    def __init__(self):
        self.__hand = []

    def sort(self):  # Selection sort as implemented from lecture slides
        '''
        Sorts all cards in hand from lowest to highest with joker as low
        Inputs: none
        Outputs: none
        '''
        for index in range(len(self.__hand)):
            smallIndex = index
            for i in range(index, len(self.__hand)):  # finding smallest
                if (self.__hand[i].getValue() < self.__hand[smallIndex].getValue()):
                    smallIndex = i

            temp = self.__hand[index]  # swapping
            self.__hand[index] = self.__hand[smallIndex]
            self.__hand[smallIndex] = temp

    def pop(self, value=None):
        '''
        Pops cards from the hand. Pop() pops highest value card; pop(n) pops at index n (note: first card in hand is indexed at 1)
        Inputs: index of desired card to pop, default is highest value card
        Outputs: card of type CardClass
        '''
        if value == None:
            return self.__hand.pop((len(self.__hand) - 1))
        else:
            return self.__hand.pop(int(value))

    def index(self, v):
        '''
        Gives index of card of value n in hand
        Inputs: value of card to search for
        Outputs: index point of card of desired value, or -1 if no such card in hand
        '''
        count = 0
        for item in self.__hand:
            if item != v:
                count += 1
            else:
                return count

    def check0(self):
        '''
        Checks hand for a card with value of 0
        Inputs: none
        Outputs: index of card with value 0, if none -1
        '''
        count = -1

        for item in self.__hand:
            count += 1
            if item == 0:
                return count
        return -1

    def size(self):
        '''
        Gives number of cards in hand
        Inputs: none
        Outputs: number of cards in hand
        '''
        return len(self.__hand)

    def add(self, card):
        '''
        Adds a card of type CardClass to a hand
        Inputs: none
        Outputs: none
        '''
        if len(self.__hand) > 4:
            raise Exception('You can not add any more cards to this hand.')
        else:
            self.__hand.append(card)

    def __str__(self):
        '''
        String conversion method
        Inputs: none
        Outputs: String representation of format: '[[][][]]'
        '''

        string = '['
        for item in self.__hand:
            string += '[' + item.getFace() + ']'
        return string + ']'


def instantiateCards():
    '''
    Creates the cardList: all 120 instantiated cards: 10 * 0-9, and 20 jokers
    Inputs: none
    Outputs: cardList: a list containing 120 card objects of type CardClass
    '''

    cardList = []

    # create 10 sets of 0 - 9
    for num in range(0, 10):
        for i in range(0, 10):
            try:
                card = CardClass(i)
            except AssertionError as i:
                print(i.args[0])
            cardList.append(card)

    # create 20 joker cards
    for n in range(0, 20):
        card = CardClass(-1)
        cardList.append(card)

    return cardList


def shuffleCards(instantiatedCards):
    '''
    Shuffles all the cards in the cardList
    Inputs: cardList (of 120 card objects)
    Outputs: shuffledDeck: a list with 120 shuffled card objects
    '''

    shuffledDeck = []

    empty = False
    listLength = 120
    while listLength != 0:
        ranNum = random.randrange(0, listLength)
        listLength -= 1
        temp = instantiatedCards.pop(ranNum)
        shuffledDeck.append(temp)

    return shuffledDeck


def createHand(shuffledDeck):
    '''
    Creates the player's hand of five card objects
    Inputs: the shuffledDeck of card objects
    Outputs: a player's hand of 5 card objects
    '''

    hand = Hand()  # Instantiate class for players' hands

    for i in range(0, 5):  # Deal out 5 cards per player
        hand.add(shuffledDeck.pop())
    return hand


def createGoalPile(Stack, shuffledDeck):
    '''
    Creates a player's Goal Pile of 15 card objects
    Inputs: class Stack, and the shuffledDeck of card objects
    Outputs: Goal Pile of 15 card objects
    '''

    goal = Stack()

    for i in range(0, 15):  # Deal out 15 cards to for a Goal Pile
        goal.push(shuffledDeck.pop())
    return goal


def instantiateDiscardPile(Stack):
    '''
    Instantiates four empty discard piles and puts them into a list
    Inputs: class Stack
    Outputs: discardList of 4 empty dicard piles (stacks)
    '''

    discardList = []

    for i in range(0, 5):
        temp = Stack()
        discardList.append(temp)
    return discardList


def playerAorB(playAhand, playBhand):
    '''
    Determines first player to begin the game accprding to highest value card
    Inputs: Both players' hands: playAhand, playBhand
    Outputs: string 'A' or string 'B'
    '''
    # Note: this function is not used in this game. A better function was designed
    if playAhand[4] >= playBhand[4]:
        return 'A'
    else:
        return 'B'


def playerSwitcher(playCounter):
    '''
    Determines when to switch players
    Inputs: playCounter: an int
    Outputs: True (player A's turn) or False (player B's turn)
    '''

    if playCounter % 2 == 0:
        return True  # Player A

    else:
        return False  # Player B


def createPlayStacks():
    '''
    Creates four empty play stacks for centre of the table, all put into a list
    Inputs: none
    Outputs: playStackList: a list of four empty play stacks
    '''

    playStackList = []

    for i in range(0, 4):
        temp = PlayStack()
        playStackList.append(temp)
    return playStackList


def printOneRound(playAhand, playAdiscardPiles, playAgoal, playStacksList, playBdiscardPiles, playBhand, playBgoal):
    '''
    Prints to screen the current state of the game
    Inputs: playAhand, playAdiscardPiles, playAgoal, playStacksList, playBdiscardPiles, playBhand, playBgoal
    Outputs: none
    '''

    print('-' * 35)

    print('PlayerA Hand', playAhand)  # Print hand

    for i in range(0, 4):  # print discard piles: check if empty, otherwise peek
        if (playAdiscardPiles[i].size()) == 0:
            print('PlayerA Discard %s:' % (playAdiscardPiles[i]))
        else:
            print('PlayerA Discard [%s]:' % (playAdiscardPiles[i].peek()))

    if not playAgoal.isEmpty():
        print('PlayerA Goal [%s] %s cards left' % (playAgoal.peek(), playAgoal.size()))
    else:
        print('Player A Goal is Empty; %s cards left' % (playAgoal.size()))

    print()

    print('Play Stack 1 :', playStacksList[0])  # Print play stacks in centre of table
    print('Play Stack 2 :', playStacksList[1])
    print('Play Stack 3 :', playStacksList[2])
    print('Play Stack 4 :', playStacksList[3])
    print()

    print('PlayerB Hand', playBhand)  # Print hand

    for i in range(0, 4):  # Print discard piles: check if empty, otherwise peek
        if (playBdiscardPiles[i].size()) == 0:
            print('PlayerB Discard %s:' % (playBdiscardPiles[i]))
        else:
            print('PlayerB Discard [%s]:' % (playBdiscardPiles[i].peek()))

    if not playBgoal.isEmpty():
        print('PlayerB Goal [%s] %s cards left' % (playBgoal.peek(), playBgoal.size()))
    else:
        print('Player B Goal is Empty; %s cards left' % (playBgoal.size()))

    print('-' * 35)


def chooseAction(playCounter):
    '''
    Prompts players for first choice in game play
    Inputs: playCounter
    Outputs: character of their choice (either 'p', or 'x')
    '''

    if playerSwitcher(playCounter):

        char = input('PlayerA, choose action: p (play) or x (discard/end turn)\n')

    else:

        char = input('PlayerB, choose action: p (play) or x (discard/end turn)\n')

    return char.lower()


def chooseCard():
    '''
    Prompts players to choose a card from one of three places: hand, goal, or discard piles
    Inputs: none
    Outputs: character and number of format cn (or just character if choosing goal pile)
    '''

    char = input('Play from where: hi = hand at position i (1..5); g = goal; dj = discard pile j (1..4)?\n')

    return char


def getCardFromHand(cardPosition, playCounter, playAhand, playBhand):
    '''
    Pops a card from player's hand according to position of their choosing
    Inputs: cardPosition, playCounter, playAhand, playBhand
    Outputs: card object of their choosing
    '''
    # cardPosition is a str eg: h3

    cardPosition = (int(
        cardPosition[1])) - 1  # cardPosition is no longer 2 chars. Get int from players choice and subtract one.

    if playerSwitcher(playCounter):

        return playAhand.pop(cardPosition)  # Returns card object

    else:
        return playBhand.pop(cardPosition)


def getHighestCardFromHand(playCounter, playAhand, playBhand):
    '''
    Gets the highest card value from a player's hand
    Inputs: playCounter, playAhand, playBhand
    Outputs: Card object of highest value
    '''
    # Special Note: This function only for use for later versions of the game

    if playerSwitcher(playCounter):

        return playAhand.pop()  # Returns card object

    else:
        return playBhand.pop()


def playCardToStack(card, playStacksList):
    '''
    Prompts player to choose a stack (1-4) and plays card object to that stack using .playCard() method
    Inputs: card (card object), playStacksList
    Outputs: none
    '''

    # Inputs: card object

    stackNum = int(input('Which Play Stack are you targeting (1..4)?'))

    playStacksList[stackNum - 1].playCard(card)


def getCardFromGoal(playCounter, playAgoal, playBgoal):
    '''
    Pops top card from player's Goal Pule
    Inputs: playCounter, playAgoal, playBgoal
    Outputs: The poped card object
    '''

    if playerSwitcher(playCounter):

        return playAgoal.pop()  # Returns card object

    else:
        return playBgoal.pop()


def loadHandAndSort(playCounter, shuffledDeck, playAhand, playBhand):
    '''
    Reloads and sorts players' hands from the shuffledDeck if hand has fewer than five cards
    Inputs: playCounter, shuffledDeck, playAhand, playBhand
    Outputs: none
    '''

    if playerSwitcher(playCounter):
        while playAhand.size() < 5:
            playAhand.add(shuffledDeck.pop())
        playAhand.sort()
    else:
        while playBhand.size() < 5:
            playBhand.add(shuffledDeck.pop())
        playBhand.sort()


def playCardToDiscardPile(cardObject, playCounter, playAdiscardPiles, playBdiscardPiles):
    '''
    Prompts player which discard pile (1-4) they would like to discard a card to and pushes the card object to that pile
    Inputs: cardObject, playCounter, playAdiscardPiles, playBdiscardPiles
    Outputs: none
    '''

    # Inputs: card object

    stackNum = int(input('Which Discard Pile are you targeting (1..4)?'))

    if playerSwitcher(playCounter):

        playAdiscardPiles[stackNum - 1].push(cardObject)  # Appends card to specified discard pile

    else:
        playBdiscardPiles[stackNum - 1].push(cardObject)


def returnCardToHand(playCounter, cardObject, playAhand, playBhand):
    '''
    Used to return a card to player's hand which was deemed unplayable
    Inputs: playCounter, cardObject, playAhand, playBhand
    Outputs: none
    '''

    if playerSwitcher(playCounter):

        playAhand.add(cardObject)  # Appends card to specified discard pile
        playAhand.sort()
        # print('Player a', playAhand)
    else:
        playBhand.add(cardObject)
        playBhand.sort()
        # print('Player a', playBhand)


def playCardFromDiscardPile(playCounter, cardPosition, playAdiscardPiles, playBdiscardPiles):
    '''
    Pops card from a discard pile for use in play
    Inputs: playCounter, cardPosition, playAdiscardPiles, playBdiscardPiles
    Outputs: card object from top of selected dicard pile
    '''
    # Outputs: Card object of Class Card

    if playerSwitcher(playCounter):
        return playAdiscardPiles[int(cardPosition[1]) - 1].pop()  # Pop from chosen discard pile

    else:
        return playBdiscardPiles[int(cardPosition[1]) - 1].pop()


def checkForWin(playAgoal, playBgoal):
    '''
    Determines if a player has won: they have emptied their goal pile
    Inputs: playAgoal, playBgoal
    Outputs: True or False
    '''
    # Return Boolean

    if playAgoal.size() == 0 or playBgoal.size() == 0:
        return True
    else:
        return False


def loadEmptyHand(playCounter, shuffledDeck, playAhand, playBhand):
    '''
    Reloads and sorts a completely empty hand
    Inputs: playCounter, shuffledDeck, playAhand, playBhand)
    Outputs: card object from top of selected dicard pile
    '''
    # Re-loads and sorts hand only if it is completely empty

    if playerSwitcher(playCounter):
        if playAhand.size() == 0:
            while playAhand.size() < 5:
                playAhand.add(shuffledDeck.pop())
            playAhand.sort()

    else:
        if playBhand.size() == 0:
            while playBhand.size() < 5:
                playBhand.add(shuffledDeck.pop())
            playBhand.sort()


def playAgain():
    '''
    Prompts user if they would like to play again
    Inputs: none
    Outputs: True or False
    '''

    answer = input('Would you like to play again? y or n?')

    if answer.lower() == 'y':
        return True
    else:
        return False


def determineFirstPlayer(playAgoal, playBgoal):
    '''
    Determines first player to begin the game accprding to highest value card
    Inputs: playAgoal, playBgoal
    Outputs: maxVal (1 = player a; 2 = player b)
    '''
    a = playAgoal.peek().getValue()
    b = playBgoal.peek().getValue()
    maxVal = None

    if a == -1 or b == -1:
        if a == -1 and b != -1:
            maxVal = 2
        if b == -1 and a != -1:
            maxVal = 1
    else:
        if playAgoal.peek().getValue() >= playBgoal.peek().getValue():
            maxVal = 2
        else:
            maxVal = 1
    return maxVal

    # if playAgoal.peek().getValue() >= playBgoal.peek().getValue():
    # return 2
    # else:
    # return 1


def chooseCardForDiscard(playCounter, playAhand, playBhand):
    '''
    Prompts player to choose a card from their hand for discarding
    Inputs: playCounter, playAhand, playBhand
    Outputs: cardPosition in hand of format character number, cn
    '''
    cardPosition = input('Which card from your hand do you wish to discard: hi = hand at position i (1..5)')

    return cardPosition


def getCardFromHandForDiscard(cardPosition, playCounter, playAhand, playBhand):
    '''
    Gets the the card object from the hand for discarding
    Inputs: cardPosition, playCounter, playAhand, playBhand
    Outputs: the card object from the hand
    '''

    cardPosition = (int(
        cardPosition[1]) - 1) - 1  # cardPosition no longer tuple. Get int from players choice and subtract one.

    if playerSwitcher(playCounter):

        assert playAhand.pop(int(cardPosition[1]) - 1) != 0  # Returns card object

    else:
        return playBhand.pop(cardPosition)


def checkForDiscardZero(cardObject):
    '''
    Checks if player is attempting to discard the card of value zero
    Inputs: card object
    Outputs: none
    '''

    if cardObject.getValue() == 0:
        raise Exception('Sorry you can not discard the value zero.')


def emptyFullPlayStacks(playStacksList, cardQuarantine):
    '''
    Empties play stacks if they fill up (if top card value is 9) and stores card objects into a list, cardQuarantine
    Inputs: playStacksList cardQuarantine
    Outputs: none
    '''
    threshold = 9  # value of card on top of stack
    for stack in playStacksList:  # check each play stack (1 - 4)
        try:
            value = stack.peekValue()  # first test if stack has any items
        except:
            pass
        else:  # if items are present in stack
            if value == threshold:  # check top card against threshold
                for num in range(threshold + 1):  # if top card value is 9, pop all cards and place in quarantine
                    card = stack.getCard()
                    cardQuarantine.append(card)
    # print('len of CQ',len(cardQuarantine))


def breakOut(playCounter):
    loop = True
    if playerSwitcher(playCounter):
        while loop:
            for stack in playStacksList:
                value = stack.peekValue()
                if playAhand.index(value + 1) != -1:
                    loop = False


        else:
            if playBhand.size() == 0:
                while playBhand.size() < 5:
                    playBhand.add(shuffledDeck.pop())
                playBhand.sort()

            # def checkForZeroInHand():

    # if playerSwitcher(playCounter):
    # if playAhand.check0() and

    # else:

