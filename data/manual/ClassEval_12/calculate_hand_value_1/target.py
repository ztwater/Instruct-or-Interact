class BlackjackGame:
    def calculate_hand_value(self, hand):
        """
        Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
        If the card is a digit, its value is added to the total hand value.
        Value of J, Q, or K is 10, while Aces are worth 11.
        If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11,
        until the hand value is less than or equal to 21, or all Aces have been counted as value of 1.
        :param hand: list
        :return: the value of the poker cards stored in hand list, a number.
        >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
        40
        """
        # Initialize the total value of the hand
        total_value = 0
        # Count the number of aces in the hand
        num_aces = 0

        # Iterate through each card in the hand
        for card in hand:
            # Get the value of the card
            if card[0] in ['J', 'Q', 'K']:
                card_value = 10
            elif card[0] == 'A':
                card_value = 11
                num_aces += 1
            else:
                card_value = int(card[0])
    
            # Add the value of the card to the total value
            total_value += card_value
    
        # Adjust the value of aces if necessary
        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1
    
        return total_value