import tkinter as tk
from Connect4Class import ConnectFour
from MinimaxClass import Minimax
import random

class GUI:
    def __init__(self):
        self.game = ConnectFour()
        self.s = 100  # Gap between centre of slots, or slots height and width, same thing
        self.r = 2*(self.s/5)  # Radius of slots
        self.c = ['grey', 'red', 'yellow']

    def win(self):
        nw = tk.Tk()
        tk.Label(nw, height=15, width=50, text='PLAYER ' + str(int((0.5*self.game.p)+1.5)) + ' WINS!!!',
                 font=('Helvetica', 50), bg='yellow').pack()
        def two():
            nw.destroy()
            self.game.restart()
            self.twoplay()
        def comp():
            nw.destroy()
            self.game.restart()
            self.compplay(1)
        tk.Button(nw, text='Play human', command=two).pack()
        tk.Button(nw, text='Play AI', command=comp).pack()

    def twoplay(self):
        w = tk.Tk()
        w.title('Connect Four')
        board = tk.Canvas(w, bg='blue', height=self.s*self.game.h, width=self.s*self.game.w)
        board.pack()
        slots = []
        check = Minimax(1, self.game)
        def update():
            print(check.count(self.game.grid))
            for x in range(self.game.w):
                for y in range(self.game.h):
                    if self.game.grid[x][y]:
                        board.itemconfig(slots[x][y], fill=self.c[self.game.grid[x][y]])

        def place(event):
            for x in range(self.game.w):
                if self.s*(0.5 + x)-self.r <= event.x <= self.s*(0.5 + x)+self.r:
                    break
            self.game.drop(x)
            if not self.game.state:
                self.win()
                w.destroy()
                return
            update()

        for x in range(self.game.w):
            col = []
            for y in range(self.game.h):
                slot = board.create_oval(self.s*(0.5 + x)-self.r, self.s*(0.5 + y)-self.r, self.s*(0.5 + x)+self.r, self.s*(0.5 + y)+self.r, fill='grey')
                board.tag_bind(slot, '<Button-1>', place)
                col.append(slot)
            slots.append(col)
        w.mainloop()

    def compplay(self, p, d):
        w = tk.Tk()
        w.title('Connect Four')
        board = tk.Canvas(w, bg='blue', height=self.s * self.game.h, width=self.s * self.game.w)
        board.pack()
        slots = []
        comp = Minimax(p, self.game)

        def update():
            for x in range(self.game.w):
                for y in range(self.game.h):
                    if self.game.grid[x][y]:
                        board.itemconfig(slots[x][y], fill=self.c[self.game.grid[x][y]])

        def win():
            for x in range(sum([sum([abs(e) for e in col]) for col in self.game.grid])):
                board.create_text(random.randint(1, self.s*self.game.h), random.randint(1, self.s*self.game.w),
                                  text='PLAYER ' + str(int((0.5*self.game.p)+1.5)) + ' WINS!!!',
                                  font='Helvetica, 50', fill='green')

        def place(event):
            for x in range(self.game.w):
                if self.s * (0.5 + x) - self.r <= event.x <= self.s * (0.5 + x) + self.r:
                    break
            self.game.drop(x)
            if not self.game.state:
                win()
            self.game.drop(comp.move(d, self.game.gridcopy())[1])
            if not self.game.state:
                win()
            update()


        for x in range(self.game.w):
            col = []
            for y in range(self.game.h):
                slot = board.create_oval(self.s * (0.5 + x) - self.r, self.s * (0.5 + y) - self.r,
                                         self.s * (0.5 + x) + self.r, self.s * (0.5 + y) + self.r, fill='grey')
                board.tag_bind(slot, '<Button-1>', place)
                col.append(slot)
            slots.append(col)

        if self.game.p*-1 == p:
            self.game.drop(3)
            update()

        w.mainloop()
