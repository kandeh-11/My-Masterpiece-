# Written by Ousman

# Question 4
'''
def find_winner(player1 = "roclk", player2 = "roc"):
    if player1 == player2:
        return "It's a tie!"
    if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"     
    
print(find_winner("rock", "scissors")) 
'''

# Question 8
'''
def decending_order(num1, num2 = 15 , num3 = 3):
    a, b, c = num1, num2, num3
    if a < b:
        a, b = b, a


    if a < c:
        a, c = c, a

    if b < c:
        b, c = c, b

    return [a, b, c]
'''
# Question 15
'''
def is_negtsive(num):
    if num < 0:
        return True
    else:
        return False

def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
    '''

class plane:
    def __init__(self, _name):
        self.name = _name

planet1 = P. lanet ("x25")