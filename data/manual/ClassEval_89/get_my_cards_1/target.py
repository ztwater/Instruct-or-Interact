class TwentyFourPointGame:
    def get_my_cards(self):
        cards = []
        for _ in range(4):
            card = random.randint(1, 9)
            cards.append(card)
        return cards