class BlackjackGame:
    def check_winner(self, player_hand, dealer_hand):
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
    
        if player_value > dealer_value:
            return "Player wins"
        elif player_value < dealer_value:
            return "Dealer wins"
        else:
            return "It's a tie"