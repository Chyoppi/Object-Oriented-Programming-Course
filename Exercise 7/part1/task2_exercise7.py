from random import randint

class DiceGame:
    def __init__(self):
        self.num_dice = 0
        self.players = {}

    def roll_dice(self, num_dice=1):
        return [randint(1, 6) for _ in range(num_dice)]

    def play_round(self):
        scores = {}
        for player_id, player in self.players.items():
            rolls = self.roll_dice(self.num_dice)
            print(f"{player} rolls: {rolls}")
            scores[player_id] = sum(rolls)

        max_score = max(scores.values())
        winners = [player for player_id, player in self.players.items() if scores[player_id] == max_score]

        if len(winners) == 1:
            print(f"{winners[0]} wins this round!")
        else:
            print(f"It's a tie between: {', '.join(str(winner) for winner in winners)}")

    def play_game(self):
        self.num_dice = int(input("How many dice do you want to roll? "))

        while True:
            self.play_round()
            play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
            if play_again != "yes":
                break

        print("Game over!")

class Mammals:
    def __init__(self, name, species, id, weight, size):
        self.name = name
        self.species = species
        self.id = id
        self.weight = weight
        self.size = size

    def __str__(self):
        return f"{self.name} (Species: {self.species}, ID: {self.id}, Weight: {self.weight}kg, Size: {self.size})"


class Player:
    def __init__(self, name, player_id, pet:Mammals):
        self._name = name
        self._player_id = player_id
        self.__pet = pet

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, value):
        self._player_id = value

    @property
    def pet(self):
        return self.__pet
    
    @pet.setter
    def pet(self, value):
        self.__pet = value

    def __str__(self):
        return f"Player {self._player_id}: {self._name}"
    

mammals_list = [
    Mammals("Mouse", "Rodent", 1, 0.2, "Tiny"),
    Mammals("Rabbit", "Lagomorph", 2, 2, "Small"),
    Mammals("Fox", "Canine", 3, 8, "Medium"),
    Mammals("Wolf", "Canine", 4, 40, "Large"),
    Mammals("Leopard", "Feline", 5, 60, "Large"),
    Mammals("Tiger", "Feline", 6, 150, "Very Large"),
    Mammals("Elephant", "Pachyderm", 7, 5000, "Massive")
]

def get_pet_by_roll(roll_sum):
    if roll_sum <= 3:
        return mammals_list[0]  # Mouse
    elif roll_sum <= 5:
        return mammals_list[1]  # Rabbit
    elif roll_sum <= 7:
        return mammals_list[2]  # Fox
    elif roll_sum <= 9:
        return mammals_list[3]  # Wolf
    elif roll_sum <= 10:
        return mammals_list[4]  # Leopard
    elif roll_sum <= 11:
        return mammals_list[5]  # Tiger
    else:
        return mammals_list[6]  # Elephant

if __name__ == "__main__":
    players = {}
    dice_game = DiceGame()

    num_players = int(input("Enter the number of players: "))
    for i in range(1, num_players + 1):
        name = input(f"Enter the name of player {i}: ")

        roll_result = dice_game.roll_dice(2)
        roll_sum = sum(roll_result)
        pet = get_pet_by_roll(roll_sum)

        print(f"{name} rolled {roll_result} (sum: {roll_sum}) and gets a {pet} as a pet.")

        player = Player(name, i, pet)
        players[i] = player

    dice_game.players = players
    dice_game.play_game()