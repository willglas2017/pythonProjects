#!/usr/bin/env python3

from os import system, name 
  
class counter():
    # define our clear function 
    def clear(self): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
      
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 
    
    def getCards(self, tot_cards):
        CARD_VALUES = {
      "0": {"val":-1, "count":tot_cards/13, "name":"Ten", "ten":True},
      "2":{"val":1, "count":tot_cards/13, "name":"Two", "ten":False},
      "3":{"val":1, "count":tot_cards/13, "name":"Three", "ten":False},
      "4":{"val":1, "count":tot_cards/13, "name":"Four", "ten":False},
      "5":{"val":1, "count":tot_cards/13, "name":"Five", "ten":False},
      "6":{"val":1, "count":tot_cards/13, "name":"Six", "ten":False},
      "7": {"val":0, "count":tot_cards/13, "name":"Seven", "ten":False},
      "8": {"val":0, "count":tot_cards/13, "name":"Eight", "ten":False},
      "9": {"val":0, "count":tot_cards/13, "name":"Nine", "ten":False},
      "A": {"val":-1, "count":tot_cards/13, "name":"Ace", "ten":False},
      "J": {"val":-1, "count":tot_cards/13, "name":"Jack", "ten":True},
      "Q": {"val":-1, "count":tot_cards/13, "name":"Queen", "ten":True},
      "K": {"val":-1, "count":tot_cards/13, "name":"King", "ten":True},
    }
        return CARD_VALUES
    
    print('Welcome to my card counter! For help at anytime, type "help". To exit, type "e"')
    
    def getDecks(self):
        try:
            user_in = input('Number of Decks\n>> ')
            decks = int(user_in)
            if decks <= 0:
                print("Error: must be 1 or more deck(s)")
                return self.getDecks()
            else:
                return decks
        except ValueError:
            if user_in == 'help':
                self.printHelp()
            elif user_in == 'e':
                return 'e'
            else:
                print('Error: please give just a number')
            return self.getDecks()
    
    def main(self):
        self.decks = self.getDecks()
        if self.decks == 'e':
            return
        tot_cards = self.decks*52
        self.ret = self.getOdds(tot_cards)
        if self.reset:
            self.reset = False
            self.main()
        
    def getOdds(self, tot_cards):
        count = 0
        cards = 0
        decks_played = 0
        CARD_VALUES = self.getCards(tot_cards)
        run = True
        print("\nEnter cards:")
        while run:
            user_input = input('>> ')
            if user_input == 'help':
                self.printHelp()
            elif user_input == 'e':
                run = False
                break
            elif user_input == 's':
                self.reset = True
                break
            else:
                for card in user_input:
                    if card.upper() in CARD_VALUES:
                        count += CARD_VALUES[card.upper()]['val']
                        CARD_VALUES[card.upper()]['count'] -= 1
                        cards += 1
                    else:
                        print("Card \"{}\" not recognized".format(card))
                decks_played = cards / 52.0
                true_count = count / (self.decks - decks_played)
                self.oddsDict = {}
                
                for c in CARD_VALUES:
                    if CARD_VALUES[c]['ten']:
                        self.oddsDict['Ten/FC'] += (CARD_VALUES[c]['count']/(tot_cards - cards))*100
                    else:
                        self.oddsDict[CARD_VALUES[c]['name']] = (CARD_VALUES[c]['count']/(tot_cards - cards))*100
                oddsList = [(x,y) for (x,y) in self.oddsDict.items()]
                oddsList.sort(key=self.takeSecond, reverse=True)
                self.clear()
                print("Input:\t{}\n".format(user_input))
                print("Probabilities:\n")
                for i in oddsList:
                    print("\t{}:\t{}%".format(i[0], round(i[1],2)))
                print('\nCount:\t{}'.format(count))
                print('True:\t{}'.format(true_count))
            return
        
    def takeSecond(self, elem):
        return elem[1]
    
    def printHelp(self):
        print('Type the cards as they\'re being dealt.\nYou can enter more than one card at a time like this:\n\n\t324 + {ENTER}\n\nOr one at a time like this:\n\n\t 3 + {ENTER} + 2 + {ENTER} + 4 + {ENTER}\n\nFor Ten, Jack, Queen, King, and Ace, type "0", "j", "q", "k", and "a"\n\nTo shuffle the deck, or change the number of decks, type "s".\n\nTo quit, type "e"')
    
    def getDict(self):
        return self.oddsDict
    
if __name__ == '__main__':
    bj = counter()
    