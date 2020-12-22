inputdata = ['Player 1:',[43,36,13,11,20,25,37,38,4,18,1,8,27,23,7,22,10,5,50,40,45,26,15,32,33],
        'Player 2:',[21,29,12,28,46,9,44,6,16,39,19,24,17,14,47,48,42,34,31,3,41,35,2,30,49]]
sample = ['Player 1:',[9,2,6,3,1],'Player 2:',[5,8,4,7,10]]

class Deck:
    def __init__(self,player,cards):
        self.player = player
        self.cards = cards
        self.score = 0
        
    def victory(self, opponentcard):
        temp = self.cards[0]
        self.cards = self.cards[1:]
        self.cards.extend([temp, opponentcard])
        
    def loss(self):
        self.cards = self.cards[1:]

def load_cards(inputlist):
    player1 = Deck(inputlist[0].strip(':'),inputlist[1])
    player2 = Deck(inputlist[2].strip(':'),inputlist[3])
    return player1, player2

def combat(p1,p2):
    while len(p1.cards) > 0 and len(p2.cards) > 0:
        if p1.cards[0] > p2.cards[0]:
            p1.victory(p2.cards[0])
            p2.loss()
        else:
            p2.victory(p1.cards[0])
            p1.loss()
    p1.score = 0
    for num, card in enumerate(p1.cards[::-1]):
        p1.score += (num+1)*card
    p2.score = 0
    for num, card in enumerate(p2.cards[::-1]):
        p2.score += (num+1)*card    
    print('Player 1:',p1.score)
    print('Player 2:',p2.score)

p1,p2 = load_cards(inputdata)
combat(p1,p2)
