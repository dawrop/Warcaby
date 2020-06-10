import tkinter as tk
from tkinter import messagebox

class Game():
    def __init__(self, parent, rows=8, columns=8, color1='white', color2='black', size=64):
        self.rows = rows
        self.columns = columns
        self.color1 = color1
        self.color2 = color2
        self.size = size
        self.parent = parent

        self.state = 0
        self.currentPawn = None

        canvas_width = self.columns * self.size
        canvas_height = self.rows * self.size
        self.border_size = 3

        self.turncanvas = tk.Canvas(parent, width=150, height=30, background='white', borderwidth=self.border_size,
                                    relief='solid', highlightbackground='white')
        self.label = tk.Label(self.turncanvas, text='Tura gracza 1')
        self.change_player_turn()
        self.turncanvas.pack()
        self.player_turn()

        self.canvas = tk.Canvas(parent, width=canvas_width, height=canvas_height, background='white',
                                borderwidth=self.border_size, relief='solid', highlightbackground='white')
        self.canvas.pack()
        self.buttons = [[tk.Button(bg='BLACK', activebackground='BLACK', fg='white') for x in range(self.rows)] for y in range(self.columns)]
        self.draw_board()


        whitescore = str(5)
        blackscore = str(7)

        self.footercanvas = tk.Canvas(parent, width=canvas_width, height=60, background='white',
                                      highlightbackground='white')
        self.scorelabel = tk.Label(self.footercanvas, text='Wynik:\nBialy: ' + whitescore + '\nCzarny: ' + blackscore,
                                   anchor=tk.NW)
        self.resetbutton = tk.Button(self.footercanvas, text='Reset', anchor=tk.N, font=('Arial', 25),
                                     command=lambda: self.change_player_turn())
        self.footercanvas.pack()
        self.scorelabel.place(x=0, y=0, height=100, width=150)
        self.resetbutton.place(x=370, y=0, height=50, width=100)

    def draw_board(self):
        color = self.color2
        for r in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for c in range(self.columns):
                x1 = (c * self.size) + self.border_size
                y1 = (r * self.size) + self.border_size
                x2 = x1 + self.size + self.border_size
                y2 = y1 + self.size + self.border_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags='area')
                color = self.color1 if color == self.color2 else self.color2
        self.buttonGrid()

    def buttonGrid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if((i + j) % 2 == 1):
                    self.buttons[i][j].place(x=i*self.size + 3, y=j*self.size + 43, width=self.size, height=self.size)

                    self.buttons[i][j]['command'] = lambda x = j, y = i: self.action(x, y)
                    if(j < 3):
                        self.buttons[i][j]['text'] = 'C'
                    if (j >= self.columns - 3):
                        self.buttons[i][j]['text'] = 'B'

    def action(self, x, y):
        if(self.processAction(x, y)):
            self.state = (self.state + 1) % 4

    def processAction(self, x, y):
        pawn = self.buttons[y][x]['text']
        print(x,y,pawn)
        if(self.state == 0 and pawn == 'C'):
            self.buttons[y][x]['text'] = '[C]'
            self.currentPawn = self.buttons[y][x]
            return True

        if(self.state == 1):
            if(pawn == '[C]'):
                self.buttons[y][x]['text'] = 'C'
                self.currentPawn = None
                self.state = self.state - 1
                return False
            if(pawn == ''):
                self.buttons[y][x]['text'] = 'C'
                self.currentPawn['text'] = ''
                self.currentPawn = None
                return True

        if (self.state == 2 and pawn == 'B'):
            self.buttons[y][x]['text'] = '[B]'
            self.currentPawn = self.buttons[y][x]
            return True

        if (self.state == 3):
            if (pawn == '[B]'):
                self.buttons[y][x]['text'] = 'B'
                self.currentPawn = None
                self.state = self.state - 1
                return False
            if (pawn == ''):
                self.buttons[y][x]['text'] = 'B'
                self.currentPawn['text'] = ''
                self.currentPawn = None
                return True

    def player_turn(self):
        self.label.place(x=5, y=5, height=30, width=150)

    def change_player_turn(self):
        if self.label['text'] == 'Tura gracza 1':
            self.label['text'] = 'Tura gracza 2'
        else:
            self.label['text'] = 'Tura gracza 1'


def main():
    root = tk.Tk()
    root.title("Warcaby")
    root.configure(bg='white')
    root.resizable(False, False)
    board = Game(root)

    root.mainloop()


if __name__ == "__main__":
    main()