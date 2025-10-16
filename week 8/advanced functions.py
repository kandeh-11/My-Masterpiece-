# Written by Ousman

# Question 4
def find_winner(player1 = "roclk", player2 = "roc"):
    if player1 == player2:
        return "It's a tie!"
    if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"     
    
print(find_winner("rock", "scissors")) 