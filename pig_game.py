import random
import argparse

random.seed(0)


class Player(object):

    def __init__(self, id_value):
        self.score = 0
        self.id = id_value

    def add_score(self, new_score):
        self.score = self.score + new_score

    def get_score(self):
        return self.score

    def get_id(self):
        return self.id

    def roll(self):
        return random.randint(1, 6)


class Game(object):

    def __init__(self, player_list):
        self.players = player_list
        self.current_active_player = player_list[0]
        self.current_active_index = 0

    def get_players_and_scores(self):
        results = {}

        for p in self.players:
            results[p.get_id()] = p.get_score()

        return results

    def get_current_active_player(self):
        return self.current_active_player

    def get_current_active_player_id(self):
        return self.current_active_player.get_id()

    def change_current_active_player(self):
        self.current_active_index += 1

        if self.current_active_index > len(self.players) - 1:
            self.current_active_index = 0

        self.current_active_player = self.players[self.current_active_index]


def game_loop(number_of_players):
    player_list = []

    winner = False

    turn_player_total = 0

    for i in range(0, number_of_players):
        new_player = Player(f"Player {i + 1}")

        player_list.append(new_player)

    game = Game(player_list)

    while not winner:

        decision = input(f"{game.get_current_active_player_id()} type 'r' to roll or type 'k' to keep your score.\n")

        while decision != 'r' and decision != 'k':
            decision = input(
                f"{game.get_current_active_player_id()} type 'r' to roll or type 'k' to keep your score.\n")

        while decision == 'r':

            current_roll = game.get_current_active_player().roll()

            if current_roll != 1:

                print(f"{game.get_current_active_player_id()} rolled a {current_roll}")

                turn_player_total += current_roll

                print(f"{game.get_current_active_player_id()} has a total roll of {turn_player_total}.")

                print(
                    f"{game.get_current_active_player_id()} would have a total score of {game.get_current_active_player().get_score() + turn_player_total}.")

                decision = input(
                    f"{game.get_current_active_player_id()} press enter to 'roll' or type 'keep' to keep your score.\n")

            else:

                print(f"{game.get_current_active_player_id()} rolled a 1 and forfeited their turn.")

                turn_player_total = 0

                decision = 'k'

        if decision == 'k':

            print(f"{game.get_current_active_player_id()} added a total of {turn_player_total} to their score.")

            game.get_current_active_player().add_score(turn_player_total)

            print(
                f"{game.get_current_active_player_id()} currently has a total score of {game.get_current_active_player().get_score()}")

            turn_player_total = 0

            if game.get_current_active_player().get_score() >= 100:

                winner = True

                print(f"Congratulations {game.get_current_active_player_id()}!")

            else:

                game.change_current_active_player()

                print(f"{game.get_current_active_player_id()} it's your turn.")


def main():
    parser = argparse.ArgumentParser(description='Pig Game.', usage="%{prog}s --numPlayers integer")
    parser.add_argument('--numPlayers', metavar='\b', required=False, type=int, help='Number of people playing.')

    args = parser.parse_args()

    number_of_players = 2

    if args.numPlayers is not None:
        number_of_players = args.numPlayers

    game_loop(number_of_players)


if __name__ == '__main__':
    main()
