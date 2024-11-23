class TwentyFourPointGame:
    def _generate_cards(self):
        cards = []
        for _ in range(9):
            card = random.randint(1, 9)
            cards.append(card)
        return cards