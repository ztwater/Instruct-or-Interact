class TwentyFourPointGame:
    def _generate_cards(self):
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        cards = []
        for _ in range(9):
            card = random.randint(1, 9)
            cards.append(card)
        return cards
