import random

moves = ['rock', 'paper', 'scissors']

class Player:
    def move(self):
        return 'rock'

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        return input("Rock, paper, or scissors? ")

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.")
        print(f"Opponent played {move2}.")
        if self.beats(move1, move2):
            print("** You win! **")
        elif self.beats(move2, move1):
            print("** Opponent wins! **")
        else:
            print("** Tie **")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"\nRound {round + 1}:")
            self.play_round()
        print("\nGame over!")

game = Game(HumanPlayer(), RandomPlayer())
game.play_game()
