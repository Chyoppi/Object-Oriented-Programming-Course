#8. Code a simple (and textual) implementation of Rock-Paper-Scissors game. Play until either you or the computer gets 3 wins. Use functions. a. Plan your game first and code piece by piece: read input from user, generate random number to get computer’s choice, then check who wins and keep track of victories. 

from random import randint

#Bots input function. It chooses randomly number between 1-3 based on input it will give rock, paper or scissors.
def rps_bot():

    random_value = randint(1,3)
    if random_value == 1:
        chosen_bot = "Rock"

    if random_value == 2:
        chosen_bot = "Paper"
    
    if random_value == 3:
        chosen_bot = "Scissors"
    
    print(f"Bot chose: {chosen_bot}")
    return chosen_bot

#Users input function and if not written correctly it will give error.
def rps_user():
    chosen_user = input("Choose [Rock, Paper, Scissors]: ")
    if chosen_user not in ["Rock", "Paper", "Scissors"]:
        print("Error! Choose [Rock, Paper, Scissors]: ")
    return chosen_user

#This checks who has won the game.
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "draw"
    elif (
        (user_choice == "Rock" and bot_choice == "Scissors") or
        (user_choice == "Paper" and bot_choice == "Rock") or
        (user_choice == "Scissors" and bot_choice == "Paper")
    ):
        return "user"
    else:
        return "bot"

#Reads past games from task8_stats.txt and it goes through for loop where it will tell how many games user/bot has won.
def past_games():
    user_stats = 0
    bot_stats = 0

    with open("task8_stats.txt", "r") as text_file:
        for x in text_file:
            x = x.strip()
            if x == "User":
                user_stats += 1
            elif x == "Bot":
                bot_stats += 1
    print(f"Bot has won {bot_stats} games and you have won {user_stats} games")
    text_file.close()

#Actual game which will run the game, if user/bot has score of 3 the game will end.
def RockPaperScissors():
    user_score = 0
    bot_score = 0

    print("Welcome to the game of Rock, Paper, Scissors!")
    past_games()
    while user_score < 3 and bot_score < 3:
        user_choice = rps_user()
        bot_choice = rps_bot()

        winner = determine_winner(user_choice, bot_choice)
        if winner == "user":
            user_score += 1
            print("You win this round!")
        elif winner == "bot":
            bot_score += 1
            print("Bot wins this round!")
        else:
            print("It's a draw!")

        print(f"Score -> You: {user_score} | Bot: {bot_score}")

    if user_score == 3:
        print("Congratulations, you won the game!")
        with open("task8_stats.txt", "a") as text_file:
            text_file.write("User\n")
            text_file.close()
    else:
        print("Bot won the game! Better luck next time.")
        with open("task8_stats.txt", "a") as text_file:
            text_file.write("Bot\n")
            text_file.close()
    
RockPaperScissors()