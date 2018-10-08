import random
import multiprocessing
import math
import time
import blackjackCounter
from tqdm import tqdm

fp = '/Users/willglas/Code/pythonProjects/blackjack/data.txt'
data = {}
max_win = 1
# configuration options
def main(odds):
    global max_win
    simulations = 10000
    num_decks = 2
    shuffle_perc = 75
    safe_odds = odds
    auto_hit = 11
    num_players = 5
    avg_hits = 1
    
    cardMap = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10, 'J':10, 'Q':10, 'K':10, 'A':1}
    
    def simulate(queue, batch_size):
        bj = blackjackCounter.counter(num_decks)
        deck = []
        
        def getOdds(player_tot):
        
            if player_tot <= auto_hit:
                return 0
            safe = 21 - player_tot
            # weird bug needs this isk why tho
            if safe <0:
                return 100
            bust_odds = 0
            if safe == 0:
                bust_odds += bj.oddsDict['A']
                for i in range(2,11):
                    bust_odds += bj.oddsDict['{}'.format(i)]
            else:
                for i in range(safe+1,11):
                    bust_odds += bj.oddsDict['{}'.format(i)]
            return bust_odds
    
        def new_deck():
            std_deck = [
    		  # 2  3  4  5  6  7  8  9  10  J   Q   K   A
    			'2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A',
    			'2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A',
    			'2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A',
    			'2', '3', '4', '5', '6', '7', '8', '9', '0', 'J', 'Q', 'K', 'A'
    		]
    
    		# add more decks
            std_deck = std_deck * num_decks
            
            random.shuffle(std_deck)
            
            bj.initialize()
            
    
            return std_deck[:]
    
        def play_hand():
            dealer_cards = []
            player_cards = []
    
    		# deal initial cards
            for j in range(2):
                for i in range(num_players):
                    a = deck.pop(0)
                    bj.inputCard(a)
                    if i == 0:
                        player_cards.append(cardMap[a])
                    elif i == num_players-1:
                        dealer_cards.append(cardMap[a])
            
    		# deal player to 12 or higher
            
            bust_odds = getOdds(sum(player_cards))
            
            a_locations = []
                    
            while bust_odds <= safe_odds:
    #            print('bust odds are {}... hit me!'.format(bust_odds))
                a = deck.pop(0)
                if a == 'A':
                    if sum(player_cards) + 11 <= 21:
                        a_locations.append(len(player_cards))
                        player_cards.append(11)
                player_cards.append(cardMap[a])
                bj.inputCard(a)
                if sum(player_cards) > 21:
    #                oldSum = sum(player_cards)
                    flag = False
                    while len(a_locations) > 0:
                        player_cards[a_locations.pop(len(a_locations)-1)] = 1
                        if sum(player_cards) <= 21:
                            flag = True
    #                        print('changed ace to 1. old sum = {}. new = {}'.format(oldSum, sum(player_cards) ))
                    if flag:
                        bust_odds = getOdds(sum(player_cards))
                        continue
                    else:
                        break
                    
                bust_odds = getOdds(sum(player_cards))
            
            for i in range(num_players-2):
                for c in range(avg_hits):
                    a = deck.pop(0)
                    bj.inputCard(a)
    		# deal dealer on soft 17
            while sum(dealer_cards) < 18:
                exit = False
                # check for soft 17
                if sum(dealer_cards) == 17:
                    exit = True
    				# check for an ace and convert to 1 if found
                    for i, card in enumerate(dealer_cards):
                        if card == 11:
                            exit = False
                            dealer_cards[i] = 1
                if exit:
                    break
                a = deck.pop(0)
                dealer_cards.append(cardMap[a])
                bj.inputCard(a)
            
            p_sum = sum(player_cards)
            d_sum = sum(dealer_cards)
    
    		
            if p_sum > 21:
                return -1;
            # dealer bust
            if d_sum > 21:
                return 1;
    		# dealer tie
            if d_sum == p_sum:
                return 0;
    		# dealer win
            if d_sum > p_sum:
                return -1;
    		# dealer lose
            if d_sum < p_sum:
                return 1
    
    	# starting deck
        deck = new_deck()
    
    	# play hands
        win = 0
        draw = 0
        lose = 0
        for i in range(0, batch_size):
    		# reshuffle cards at shuffle_perc percentage
            if (float(len(deck)) / (52 * num_decks)) * 100 < shuffle_perc:
                deck = new_deck()
    
    		# play hand
            result = play_hand()
    
    		# tally results
            if result == 1:
                win += 1
            elif result == 0:
                draw += 1
            elif result == -1:
                lose += 1
    
    	# add everything to the final results
        queue.put([win, draw, lose])
    
    
    start_time = time.time()
    
    # simulate
    cpus = multiprocessing.cpu_count()
    batch_size = int(math.ceil(simulations / float(cpus)))
    
    queue = multiprocessing.Queue()
    
    # create n processes
    processes = []
    
    for i in range(0, cpus):
        process = multiprocessing.Process(target=simulate, args=(queue, batch_size))
        processes.append(process)
        process.start()
    
    # wait for everything to finish
    for proc in processes:
        proc.join()
    
    finish_time = time.time() - start_time
    
    # get totals
    win = 0
    draw = 0
    lose = 0
    
    for i in range(0, cpus):
        results = queue.get()
        win += results[0]
        draw += results[1]
        lose += results[2]
    
#    print
#    print ('  cores used: %d' % cpus)
#    print ('  total simulations: %d' % simulations)
#    print ('  simulations/s: %d' % (float(simulations) / finish_time))
#    print ('  execution time: %.2fs' % finish_time)
#    print ('  win percentage: %.2f%%'  % ((win / float(simulations)) * 100))
#    print ('  draw percentage: %.2f%%' % ((draw / float(simulations)) * 100))
#    print ('  lose percentage: %.2f%%' % ((lose / float(simulations)) * 100))
#    print
#    
    data[win/lose] = '{}'.format(safe_odds)
        
if __name__ == '__main__':
    for i in tqdm(range(20, 90)):
        main(i)
    