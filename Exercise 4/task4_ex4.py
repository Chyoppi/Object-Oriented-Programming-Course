
class LunchCard:
    def __init__(self, balance:float):
        self.balance = balance
    
    def __str__(self):
        return f"The balance is {self.balance:.1f} euros."
    
    def eat_ordinary(self):
        if self.balance < 2.95:
            print("Not enough money on the card.")
        
        else:
            self.balance -= 2.95

    def eat_luxury(self):
        if self.balance < 5.90:
            print("Not enough money on the card.")
        
        else:
            self.balance -= 5.90

    def deposit_money (self, value:float):
        if value < 0:
            raise ValueError("You cannot deposit negative money.")
        else:
            self.balance += value

#Part 1
card = LunchCard(50)
print(card)

#Part 2

card.eat_ordinary()
print(card)

card.eat_luxury()
print(card)

#Part 3
card.deposit_money(20)
print(card)

#Part 4
card_peter = LunchCard(20)
card_grace = LunchCard(30)

card_peter.eat_luxury()
card_grace.eat_ordinary()

print(f"Peter: {card_peter}")
print(f"Grace: {card_grace}")

card_peter.deposit_money(20)

card_grace.eat_luxury()

print(f"Peter: {card_peter}")
print(f"Grace: {card_grace}")

card_peter.eat_ordinary()
card_peter.eat_ordinary()

card_grace.deposit_money(50)

print(f"Peter: {card_peter}")
print(f"Grace: {card_grace}")