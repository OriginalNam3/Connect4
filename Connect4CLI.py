from Connect4Class import ConnectFour
from MinimaxClass import Minimax

class CLI:
    def __init__(self):
        self.game = ConnectFour()

    def change(self, c):
        if c == 0: return 0
        else: return int(c*0.5+1.5)

    def display(self):
        for i in range(self.game.h):
            print([self.change(self.game.grid[j][i]) for j in range(self.game.w)])
        print([1, 2, 3, 4, 5, 6, 7])

    def twoplay(self):
        while not self.game.full() and self.game.state:
            for _ in range(2):
                self.display()
                print('Player ', int((self.game.p * 0.5) + 1.5), " to move.")
                col = ''
                while not col.isdigit() or not self.game.valid(int(col)-1): col = input('Column: ')
                self.game.drop(int(col)-1)
                if not self.game.state:
                    print('Player ', int((p * 0.5) + 1.5), ' Won !!!!')
                    break
        print('Game Over.')

    # def compplay(self, p, d):
    #     comp = Minimax(p, self.game)
    #     while not self.game.full() and self.game.state:
    #         for turn in [-1, 1]:
    #             if turn == p: self.game.drop(comp.move(d), p)
    #             else:
    #                 self.display()
    #                 print("Player's move.")
    #                 col = ''
    #                 while not col.isdigit() or not self.game.valid(int(col) - 1): col = input('Column: ')
    #                 self.game.drop(int(col) - 1, turn)
