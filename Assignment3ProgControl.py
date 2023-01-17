# Assignment 3

from SpiteAndMalice import *
from LectureStructures import Stack


# SpiteAndMalice Functions List: CardClass, PlayStack, Hand, instantiateCards, shuffleCards, createHand, createGoalPile, instantiateDiscardPile, printOneRound, createPlayStacks, chooseAction, chooseCard, playerAorB, playerSwitcher, getCardFromHand, playCardToStack, getCardFromGoal, loadHandAndSort, playCardToDiscardPile, getHighestCardFromHand, returnCardToHand, playCardFromDiscardPile, checkForWin, loadEmptyHand, playAgain


def main():
    newGame = True
    while newGame:  # Fresh game starts here; instantiate cards, shuffle the deck, deal cards out

        ##################################################
        ##### Create cardList containing all cards:  #####
        #####  10 sets of 0 - 9; and 20 '*' cards    #####
        ##################################################

        cardList = instantiateCards()  # returns a list of all card objects

        # print('card list:               ',cardList)
        # print('length of cardlist:',len(cardList))
        # print()

        ##################################################
        #####   Shuffle cards from cardList         ######
        ##################################################

        shuffledDeck = shuffleCards(cardList)  # Aka 'the shoe'

        # print('Shuffled deck:           ',shuffledDeck)
        # print('length of shuffled deck:',len(shuffledDeck))
        # print()
        # -------------------------------------------------------

        ##################################################
        #####   Deal out cards to both players       #####
        #####    5 to hands, 15 to Goal Piles        #####
        ##################################################

        playAhand = createHand(shuffledDeck)  # Create hands for both players. Returns Class Hand
        playBhand = createHand(shuffledDeck)

        playAhand.sort()  # Sort both players' hands from lowest to highest
        playBhand.sort()

        # print('Player a hand:',playAhand)
        # print('Player b hand:',playBhand)
        # print()

        playAgoal = createGoalPile(Stack, shuffledDeck)  # Create Goal Piles for both players. Returns stack
        playBgoal = createGoalPile(Stack, shuffledDeck)

        # print('Player a Goal:',playAgoal)
        # print('Player b Goal:',playBgoal)
        # print()
        # print('length of shuffled deck:',len(shuffledDeck))
        # print()

        ##################################################
        ###  Instantiate Discard Piles; returns a list ###
        ###       4 Discard Piles per player           ###
        ##################################################

        playAdiscardPiles = instantiateDiscardPile(
            Stack)  # Create discard piles for both players as a list of 4 Stacks from LectureStructures [...]
        playBdiscardPiles = instantiateDiscardPile(Stack)

        ##################################################
        ###         Create List of Play Stacks         ###
        ##################################################

        playStacksList = createPlayStacks()  # Create play stacks for centre of table; returns list with 4 stacks inside

        print()

        # Initialize playCounter so that the first player is determined by the value of top card on Goal Stack; joker is high.
        playCounter = determineFirstPlayer(playAgoal, playBgoal)

        mainGame = True
        cardQuarantine = []
        while mainGame:  # Reloads hand after a player finishes their round

            playerLoop = True

            loadHandAndSort(playCounter, shuffledDeck, playAhand,
                            playBhand)  # Confirm hand is fully loaded; if not, add needed cards

            printOneRound(playAhand, playAdiscardPiles, playAgoal, playStacksList, playBdiscardPiles, playBhand,
                          playBgoal)

            while playerLoop:  # A single player's round occurs inside this loop

                actionChoice = chooseAction(playCounter)  # Get first choice from player

                if actionChoice == 'p':  # If choosing to 'play'

                    promptLoop = True  # The prompts following the 'play' choice

                    while promptLoop:

                        cardPosition = chooseCard()  # 'play from where?' Returns a a str, eg: h3

                        if cardPosition[0] == 'h':

                            cardObject = getCardFromHand(cardPosition, playCounter, playAhand, playBhand)

                            try:  # Checking: 1. if list is empty (and thus can only take 0 or *), or 2. that correct value of card is given

                                playCardToStack(cardObject,
                                                playStacksList)  # Contains call to playcard() which tests for correct values

                            except Exception as i:  # Return illegal card to hand

                                print(i.args[0])
                                returnCardToHand(playCounter, cardObject, playAhand, playBhand)

                            else:
                                # Empty any plays stacks which are full, re-load and sort hand if it goes empty while playing: Returns True if re-load required
                                emptyFullPlayStacks(playStacksList, cardQuarantine)
                                loadEmptyHand(playCounter, shuffledDeck, playAhand, playBhand)
                                promptLoop = False

                        if cardPosition[0] == 'g':
                            cardObject = getCardFromGoal(playCounter, playAgoal, playBgoal)
                            playCardToStack(cardObject, playStacksList)
                            emptyFullPlayStacks(playStacksList, cardQuarantine)
                            promptLoop = False

                        if cardPosition[0] == 'd':
                            cardObject = playCardFromDiscardPile(playCounter, cardPosition, playAdiscardPiles,
                                                                 playBdiscardPiles)
                            playCardToStack(cardObject, playStacksList)
                            emptyFullPlayStacks(playStacksList, cardQuarantine)
                            promptLoop = False

                    # Only printed when promptLoop == False
                    printOneRound(playAhand, playAdiscardPiles, playAgoal, playStacksList, playBdiscardPiles, playBhand,
                                  playBgoal)

                    if checkForWin(playAgoal, playBgoal):  # Check for win after each player finishes their round
                        if playerSwitcher(playCounter):
                            player = 'A'
                        else:
                            player = 'B'
                        print('Congratulations, player%s you win!' % (player))

                        if not playAgain():
                            mainGame = False
                            playerLoop = False
                            newGame = False
                        else:
                            mainGame = False
                            playerLoop = False

                elif actionChoice == 'x':  # If choosing to 'discard/end turn'

                    promptLoop2 = True  # The prompts following the 'x' choice

                    while promptLoop2:

                        cardPosition = chooseCardForDiscard(playCounter, playAhand, playBhand)
                        cardObject = getCardFromHand(cardPosition, playCounter, playAhand, playBhand)
                        try:  # Checking if card to discard is legal (not 0)

                            checkForDiscardZero(cardObject)

                        except Exception as i:

                            print(i.args[0])
                            returnCardToHand(playCounter, cardObject, playAhand, playBhand)

                        else:
                            playCardToDiscardPile(cardObject, playCounter, playAdiscardPiles, playBdiscardPiles)
                            promptLoop2 = False

                    playerLoop = False
                    playCounter += 1

    print('Thank you for playing Spite and Malice!')  # Final message if player chooses not to start a new game


main()

# if __name__ == "__main__":

# cardList = instantiateCards()

# print('card list:               ',cardList)
# print('length of cardlist:',len(cardList))
# print()


# shuffledDeck = shuffleCards(cardList)

# print('Shuffled deck:           ',shuffledDeck)
# print('length of shuffled deck:',len(shuffledDeck))
# print()


# playAhand = createHand(shuffledDeck) # Create hands for both players. Returns Class Hand
# playBhand = createHand(shuffledDeck)

# playAhand.sort() # Sort both players' hands from lowest to highest
# playBhand.sort()

# print('Player a hand:',playAhand)
# print('Player b hand:',playBhand)
# print()

# playAgoal = createGoalPile(Stack, shuffledDeck) # Create Goal Piles for both players. Returns stack
# playBgoal = createGoalPile(Stack, shuffledDeck)

# print('Player a Goal:',playAgoal)
# print('Player b Goal:',playBgoal)
# print()
# print('length of shuffled deck:',len(shuffledDeck))
# print()
