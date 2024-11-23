class BlackjackGame:
    def check_winner(player_hand, dealer_hand):
        player_value = sum(player_hand)
        dealer_value = sum(dealer_hand)
    
        if player_value > dealer_value:
            return "Player wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"