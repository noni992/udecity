import random
import time


moves = ['rock', 'paper', 'scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# A P2 that always plays 'rock'.

class Player:
    p1 = random.choice(moves)
    p2 = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, p1, p2):
        pass


# A P2 that chooses its moves randomly.

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, p1, p2):
        pass


# P1 can play and write his choice.

class HumanPlayer(Player):
    def move(self):
        while True:
            Human_Input = input("Choose your move: Rock, Paper or Scissors:\n")
            if Human_Input.lower() not in moves:
                print("Invalid Move Please choose Rock, Paper or Scissors")
            else:  # if there is no typo it will continue the game.
                return Human_Input


# A p2 that cycles through the three moves.

class CyclePlayer(Player):
    def learn(self, p1, p2):
        self.p1 = p1

    def move(self):
        for cycle in moves:
            if self.p1 == 'scissors':
                return 'paper'
            elif self.p1 == 'paper':
                return 'rock'
            else:
                return 'scissors'


# A p2 that remembers and imitates.

class ReflectPlayer:
    def __init__(self):
        super().__init__()
        self.p2 = None

    def learn(self, p1, p2):
        self.p2 = p2

    def move(self):
        if self.p2 is None:
            return random.choice(moves)
        return self.p2


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.point_1 = 0
        self.point_2 = 0

    def beats(self, one, two):
        return (
               (one == "rock" and two == "scissors") or
               (one == "scissors" and two == "paper") or
               (one == "paper" and two == "rock")
               )

    def play_game(self):
        print_pause("We will play Rock, paper, scissors game.")
        print_pause("It's an old game and for sure you know it.")
        print_pause("We will play 3 rounds only.")
        print_pause("So Lets start now!")
        for round in range(3):
            print_pause(f"Round {round}:")
            self.play_round()
            print_pause(f"Score: Player1 = {self.point_1}"
                        f" and Player2 = {self.point_2}")
            if self.point_1 > self.point_2:
                print("You Won!!")
            elif self.point_1 < self.point_2:
                print("You Lost!!")
        print("Game Over")

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print_pause(f"Player1: {move1} Player2: {move2}")
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

        if self.beats(move1, move2) is True:
            print_pause("Player1 gets a point!")
            self.point_1 += 1
        elif self.beats(move2, move1) is True:
            print_pause("Player2 gets a point!")
            self.point_2 += 1
        else:
            print_pause("That was a tie")


strategies = {
              "1": Player(),
              "2": RandomPlayer(),
              "3": CyclePlayer(),
              "4": ReflectPlayer()
              }

user_input = input("Select the player strategy "
                   "you want to play against\n"
                   "1- Rock Player\n"
                   "2- Random Player\n"
                   "3- Cycle Player\n"
                   "4- Reflect Player\n")

if __name__ == '__main__':
    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
