class BlackjackGame:
    def calculate_hand_value(self, hand):
        total_value = 0
        num_aces = 0
    
        for card in hand:
            if card in ['J', 'Q', 'K']:
                card_value = 10
            elif card == 'A':
                card_value = 11
                num_aces += 1
            else:
                card_value = int(card)
    
            total_value += card_value
    
        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1
    
        return total_value