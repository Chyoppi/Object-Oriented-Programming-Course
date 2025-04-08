import json

class HockeyStats:
    def __init__(self, filename):
        self.players = self.load_data(filename)

    def load_data(self, filename):
        with open(filename) as f:
            return json.load(f)

    def search_player(self, name):
        for player in self.players:
            if player['name'].lower() == name.lower():
                return player
        return None

    def get_teams(self):
        return sorted(set(p['team'] for p in self.players))

    def get_countries(self):
        return sorted(set(p['nationality'] for p in self.players))

    def players_in_team(self, team):
        return sorted(
            [p for p in self.players if p['team'] == team],
            key=lambda p: (-(p['goals'] + p['assists']), -p['goals'])
        )

    def players_from_country(self, country):
        return sorted(
            [p for p in self.players if p['nationality'] == country],
            key=lambda p: (-(p['goals'] + p['assists']), -p['goals'])
        )

    def most_points(self, n):
        return sorted(
            self.players,
            key=lambda p: (-(p['goals'] + p['assists']), -p['goals'])
        )[:n]

    def most_goals(self, n):
        return sorted(
            self.players,
            key=lambda p: (-p['goals'], p['games'])
        )[:n]

    def format_player(player):
        name = player['name']
        team = player['team']
        goals = player['goals']
        assists = player['assists']
        points = goals + assists
        return f"{name:>20} {team:>4} {goals:>3} + {assists:<3} = {points:>3}"


class Terminal:
    def __init__(self):
        while True:
            filename = input("File name: ")
            try:
                self.hockey = HockeyStats(filename)
                print(f"read the data of {len(self.hockey.players)} players")
                break
            except FileNotFoundError:
                print("File not found.")
                self.hockey = None

    def run(self):
        if not self.hockey:
            return

        while True:
            self.print_menu()
            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.search_player()
            elif command == "2":
                self.list_teams()
            elif command == "3":
                self.list_countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.list_most_points()
            elif command == "7":
                self.list_most_goals()
            else:
                print("Invalid command")

    def print_menu(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_player(self):
        name = input("name: ")
        player = self.hockey.search_player(name)
        if player:
            print(HockeyStats.format_player(player))
        else:
            print("Player not found")

    def list_teams(self):
        print("\n".join(self.hockey.get_teams()))

    def list_countries(self):
        print("\n".join(self.hockey.get_countries()))

    def players_in_team(self):
        team = input("team: ")
        for p in self.hockey.players_in_team(team):
            print(HockeyStats.format_player(p))

    def players_from_country(self):
        country = input("country: ")
        for p in self.hockey.players_from_country(country):
            print(HockeyStats.format_player(p))

    def list_most_points(self):
        n = int(input("how many: "))
        for p in self.hockey.most_points(n):
            print(HockeyStats.format_player(p))

    def list_most_goals(self):
        n = int(input("how many: "))
        for p in self.hockey.most_goals(n):
            print(HockeyStats.format_player(p))

if __name__ == "__main__":
    Terminal().run()
