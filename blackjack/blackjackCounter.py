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
    
#    print('Welcome to my card counter! For help at anytime, type "help". To exit, type "e"')
    
    
    def __init__(self, decks):
        self.decks = decks
        self.tot_cards = self.decks*52
        self.initialize()
        
        
    def initialize(self):
        self.count = 0
        self.cards = 0
        self.decks_played = 0
        self.CARD_VALUES = self.getCards(self.tot_cards)
        self.oddsDict = {}
        
    def takeSecond(self, elem):
        return elem[1]
    
    def printHelp(self):
        print('Type the cards as they\'re being dealt.\nYou can enter more than one card at a time like this:\n\n\t324 + {ENTER}\n\nOr one at a time like this:\n\n\t 3 + {ENTER} + 2 + {ENTER} + 4 + {ENTER}\n\nFor Ten, Jack, Queen, King, and Ace, type "0", "j", "q", "k", and "a"\n\nTo shuffle the deck, or change the number of decks, type "s".\n\nTo quit, type "e"')
    

    def inputCard(self, ui):
        user_input = ui
        for card in user_input:
            if card.upper() in self.CARD_VALUES:
                self.count += self.CARD_VALUES[card.upper()]['val']
                self.CARD_VALUES[card.upper()]['count'] -= 1
                self.cards += 1
            else:
                print("Card \"{}\" not recognized".format(card))
        decks_played = self.cards / 52.0
        self.true_count = self.count / (self.decks - decks_played)
        self.oddsDict = {}
        self.oddsDict['10'] = 0
        for c in self.CARD_VALUES:
            if self.CARD_VALUES[c]['ten']:
                self.oddsDict['10'] += (self.CARD_VALUES[c]['count']/(self.tot_cards - self.cards))*100
            else:
                self.oddsDict[c] = (self.CARD_VALUES[c]['count']/(self.tot_cards - self.cards))*100
        return self.oddsDict
    
    
if __name__ == '__main__':
    bj = counter(4)
    x = bj.inputCard('2345a')