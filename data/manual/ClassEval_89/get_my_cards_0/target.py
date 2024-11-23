class TwentyFourPointGame:
    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        cards = []
        for _ in range(4):
            card = random.randint(1, 9)
            cards.append(card)
        return cards