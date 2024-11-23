class BlackjackGame:
    def check_winner(self, player_hand, dealer_hand):
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value <= 21 and dealer_value <= 21:
            if abs(21 - player_value) < abs(21 - dealer_value):
                return "Player wins"
            elif abs(21 - dealer_value) < abs(21 - player_value):
                return "Dealer wins"
            else:
                return "It's a tie"
        elif player_value <= 21 and dealer_value > 21:
            return "Player wins"
        elif player_value > 21 and dealer_value <= 21:
            return "Dealer wins"
        else:
            if player_value < dealer_value:
                return "Player wins"
            elif player_value > dealer_value:
                return "Dealer wins"
            else:
                return "It's a tie"