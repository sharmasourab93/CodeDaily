import collections

Card=collections.namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]
    suits='spade diamond heart club'.split()
    
    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits
                    for rank in self.ranks]
        
        
    def __len__(self): return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


beer_card=Card('7','diamond')
deck=FrenchDeck()
print(deck[3:12])
print(beer_card,len(deck))