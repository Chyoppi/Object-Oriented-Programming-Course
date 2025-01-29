"""Modify the toss_the_coin() function so that there are 3 more options:  

1.Coin lands on the table upright (and not flat showing heads or tails)
2.Coin drops on the ground and disappears in a rabbit hole
3.Coin defies gravity and gets lost on a wormhole in space.  

Give the different options different likelyhoods, so that the heads and tails are the most likely ones,and the rest are less likely so that the option three is the least likeliest to happen. 
Name the options properly and give informative and readable output of the status."""


import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"
    
    def toss_the_coin(self):
        toss_value = random.randint(0, 150)

        if toss_value < 50:
            self.sideup = "Heads"
        elif toss_value > 100:
            self.sideup = "Tails"
        elif 76 <= toss_value <= 80:
            self.sideup = "Coin has landed upright on the table DRAW!"
        elif 81 <= toss_value <= 100:
            self.sideup = "Coin has landed on the floor and disappeared in rabbit hole DRAW!"
        elif 50 <= toss_value <= 75:
            self.sideup = "Coin was lost in wormhole DRAW!"

    def get_sideup(self):
        return self.sideup
    
def main():
    my_coin = Coin()
    print("This side is up:", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now this side is up:", my_coin.get_sideup())

main()