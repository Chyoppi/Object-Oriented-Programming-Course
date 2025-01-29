import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"
    
    def toss_the_coin(self):
        toss_value = random.randint(0, 100)

        if toss_value < 48:
            self.sideup = "Heads"
        elif toss_value > 51:
            self.sideup = "Tails"
        elif toss_value == 49:
            self.sideup = "Coin has landed upright on the table DRAW!"
        elif toss_value == 50:
            self.sideup = "Coin has landed on the floor and disappeared in rabbit hole DRAW!"
        elif toss_value == 51:
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