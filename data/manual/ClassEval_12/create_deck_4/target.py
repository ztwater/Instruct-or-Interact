class BlackjackGame:
    def create_deck(self):
        """
        Create a deck of 52 cards, which stores 52 rondom order poker with the Jokers removed.
        :return: a list of 52 rondom order poker with the Jokers removed, format is ['AS', '2S', ...].
        """
        suits = ['S', 'D', 'C', 'H']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        deck = []
        
        for suit in suits:
            for rank in ranks:
                card = rank + suit
                deck.append(card)
        
        random.shuffle(deck)
        
        return deck