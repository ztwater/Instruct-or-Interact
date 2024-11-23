class BlackjackGame:
    def check_winner(self, player_hand, dealer_hand):
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
    
        if player_value <= 21 and dealer_value <= 21:
            if abs(player_value - 21) < abs(dealer_value - 21):
                return "Player wins!"
            elif abs(player_value - 21) > abs(dealer_value - 21):
                return "Dealer wins!"
            else:
                return "It's a tie!"
        elif player_value > 21 and dealer_value > 21:
            return "It's a tie!"
        elif player_value <= 21 and dealer_value > 21:
            return "Player wins!"
        else:
            return "Dealer wins!"