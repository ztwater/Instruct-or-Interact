class BlackjackGame:
    def create_deck(self):
        suits = ['S', 'H', 'D', 'C']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
        deck = []
    
        for suit in suits:
            for rank in ranks:
                card = rank + suit
                deck.append(card)
    
        random.shuffle(deck)
    
        return deck