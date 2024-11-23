class BlackjackGame:
    def calculate_hand_value(hand):
        # Initialize the total value of the hand
        total_value = 0
        # Count the number of aces in the hand
        num_aces = 0
    
        # Iterate through each card in the hand
        for card in hand:
            # Get the value of the card
            if card in ['J', 'Q', 'K']:
                card_value = 10
            elif card == 'A':
                card_value = 11
                num_aces += 1
            else:
                card_value = int(card)
    
            # Add the value of the card to the total value
            total_value += card_value
    
        # Adjust the value of aces if necessary
        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1
    
        return total_value