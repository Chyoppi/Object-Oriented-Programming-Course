import random 

class WordGame():
    def __init__(self, rounds: int): 
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1: 
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2: 
                self.wins2 += 1
                print("player 2 won")
            else:
                pass
    
class LongestWord(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return random.randint(1, 2)
        
class VowelCount(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if player1_word.count("a") + player1_word.count("e") + player1_word.count("i") + player1_word.count("o") + player1_word.count("u") > player2_word.count("a") + player2_word.count("e") + player2_word.count("i") + player2_word.count("o") + player2_word.count("u"):
            return 1
        elif player1_word.count("a") + player1_word.count("e") + player1_word.count("i") + player1_word.count("o") + player1_word.count("u") < player2_word.count("a") + player2_word.count("e") + player2_word.count("i") + player2_word.count("o") + player2_word.count("u"):
            return 2
        else:
            return random.randint(1, 2)
        
class RockPaperScissorLizardSpock(WordGame):
    def round_winner(self, player1_word: str, player2_word: str):
        if player1_word == player2_word:
            return 0
        elif player1_word == "Scissors" and player2_word == "Paper":
            return 1
        elif player1_word == "Paper" and player2_word == "Rock":
            return 1
        elif player1_word == "Rock" and player2_word == "Lizard":
            return 1
        elif player1_word == "Lizard" and player2_word == "Spock":
            return 1
        elif player1_word == "Spock" and player2_word == "Lizard":
            return 1
        elif player1_word == "Scissors" and player2_word == "Lizard":
            return 1
        elif player1_word == "Lizard" and player2_word == "Paper":
            return 1
        elif player1_word == "Paper" and player2_word == "Spock":
            return 1
        elif player1_word == "Spock" and player2_word == "Rock":
            return 1
        elif player1_word == "Rock" and player2_word == "Scissors":
            return 1
        else:
            return 2