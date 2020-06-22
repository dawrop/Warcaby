import tkinter as tk
from tkinter import messagebox
import math

PLAYER_1 = '♟'
PLAYER_2 = '♙'
PLAYER_1_QUEEN = '♛'
PLAYER_2_QUEEN = '♕'

PLAYER_1_SELECT = f"[{PLAYER_1}]"
PLAYER_2_SELECT = f"[{PLAYER_2}]"
PLAYER_1_QUEEN_SELECT = f"[{PLAYER_1_QUEEN}]"
PLAYER_2_QUEEN_SELECT = f"[{PLAYER_2_QUEEN}]"


class Game():
    def __init__(self, parent, rows=8, columns=8, color1='white', color2='grey', size=64):
        self.rows = rows
        self.columns = columns
        self.color1 = color1
        self.color2 = color2
        self.size = size
        self.parent = parent

        self.state = 0
        self.currentPawn = None
        self.whitescore = 0
        self.blackscore = 0

        canvas_width = self.columns * self.size
        canvas_height = self.rows * self.size
        self.border_size = 3

        self.turncanvas = tk.Canvas(parent, width=150, height=30, background='white', borderwidth=self.border_size,
                                    relief='solid', highlightbackground='white')
        self.label = tk.Label(self.turncanvas)
        self.change_player_turn()
        self.turncanvas.pack()
        self.player_turn()

        self.canvas = tk.Canvas(parent, width=canvas_width, height=canvas_height, background='white',
                                borderwidth=self.border_size, relief='solid', highlightbackground='white')
        self.canvas.pack()
        self.buttons = [[tk.Button(bg='grey', activebackground='grey', fg='white', font=('Arial', 30, 'bold')) for x in
                         range(self.rows)] for y in range(self.columns)]
        self.draw_board()

        self.footercanvas = tk.Canvas(parent, width=canvas_width, height=60, background='white',
                                      highlightbackground='white')
        self.scorelabel = tk.Label(self.footercanvas,
                                   text='Wynik:\nBialy: ' + str(self.whitescore) + '\nCzarny: ' + str(self.blackscore),
                                   anchor=tk.NW)

        self.resetbutton = tk.Button(self.footercanvas, text='Reset', anchor=tk.N, font=('Arial', 25),
                                     command=lambda: self.reset_fun())
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
                if ((i + j) % 2 == 1):
                    self.buttons[i][j].place(x=i * self.size + 4, y=j * self.size + 44, width=self.size,
                                             height=self.size)
                    self.buttons[i][j]['command'] = lambda x=j, y=i: self.action(x, y)
                    setattr(self.buttons[i][j], 'x', j)
                    setattr(self.buttons[i][j], 'y', i)

                    if (j < 3):
                        self.buttons[i][j]['text'] = PLAYER_1
                        self.buttons[i][j]['fg'] = 'black'
                    elif (j >= self.columns - 3):
                        self.buttons[i][j]['text'] = PLAYER_2
                        self.buttons[i][j]['fg'] = 'white'
                    else:
                        self.buttons[i][j]['text'] = ''

    def reset_fun(self):
        self.state = 0
        self.label['text'] = 'Tura gracza 1'
        self.whitescore = 0
        self.blackscore = 0
        self.buttonGrid()
        self.update_score()

    def update_score(self):
        self.scorelabel['text'] = 'Wynik:\nBialy: ' + str(self.whitescore) + '\nCzarny: ' + str(
            self.blackscore)

    def action(self, x, y):
        if (self.processAction(x, y)):
            self.state = (self.state + 1) % 4
        if self.buttons[y][x]['text'] == PLAYER_1 or self.buttons[y][x]['text'] == PLAYER_1_SELECT \
               or self.buttons[y][x]['text'] == PLAYER_1_QUEEN or self.buttons[y][x]['text'] == PLAYER_1_QUEEN_SELECT:
            self.buttons[y][x]['fg'] = 'black'
        else:
            self.buttons[y][x]['fg'] = 'white'
        self.change_player_turn()

    def processAction(self, x, y):
        pawn = self.buttons[y][x]
        if (self.state == 0 and pawn['text'] == PLAYER_1):
            self.buttons[y][x]['text'] = PLAYER_1_SELECT
            self.currentPawn = self.buttons[y][x]
            return True

        if (self.state == 0 and pawn['text'] == PLAYER_1_QUEEN):
            self.buttons[y][x]['text'] = PLAYER_1_QUEEN_SELECT
            self.currentPawn = self.buttons[y][x]
            return True

        if (self.state == 1):
            if pawn == self.currentPawn:
                if self.currentPawn['text'] == PLAYER_1_QUEEN_SELECT:
                    self.buttons[y][x]['text'] = PLAYER_1_QUEEN
                else:
                    self.buttons[y][x]['text'] = PLAYER_1
                self.currentPawn = None
                self.state = self.state - 1
                return False

            if (pawn['text'] == ''):
                efekt = self.check_valid_move(self.currentPawn.x, self.currentPawn.y, x, y)
                if (efekt):
                    if x == 7 or self.currentPawn['text'] == PLAYER_1_QUEEN_SELECT:
                        self.buttons[y][x]['text'] = PLAYER_1_QUEEN
                    else:
                        self.buttons[y][x]['text'] = PLAYER_1
                    self.currentPawn['text'] = ''
                    if (efekt == 'z'):
                        self.currentPawn = self.buttons[y][x]
                        if self.currentPawn['text'] == PLAYER_1_QUEEN:
                            self.currentPawn['text'] = PLAYER_1_QUEEN_SELECT
                        else:
                            self.currentPawn['text'] = PLAYER_1_SELECT
                        self.blackscore = self.blackscore + 1
                        self.update_score()
                        end(self.blackscore, self.whitescore)
                        return False
                    else:
                        self.currentPawn = None
                else:
                    return False
                return True

        if (self.state == 2 and pawn['text'] == PLAYER_2):
            self.buttons[y][x]['text'] = PLAYER_2_SELECT
            self.currentPawn = self.buttons[y][x]
            return True

        if (self.state == 2 and pawn['text'] == PLAYER_2_QUEEN):
            self.buttons[y][x]['text'] = PLAYER_2_QUEEN_SELECT
            self.currentPawn = self.buttons[y][x]
            return True

        if (self.state == 3):
            if pawn == self.currentPawn:
                if self.currentPawn['text'] == PLAYER_2_QUEEN_SELECT:
                    self.buttons[y][x]['text'] = PLAYER_2_QUEEN
                else:
                    self.buttons[y][x]['text'] = PLAYER_2
                self.currentPawn = None
                self.state = self.state - 1
                return False
            if (pawn['text'] == ''):
                efekt = self.check_valid_move(self.currentPawn.x, self.currentPawn.y, x, y)
                # print(efekt)
                if (efekt):
                    if x == 0 or self.currentPawn['text'] == PLAYER_2_QUEEN_SELECT:
                        self.buttons[y][x]['text'] = PLAYER_2_QUEEN
                    else:
                        self.buttons[y][x]['text'] = PLAYER_2
                    self.currentPawn['text'] = ''
                    if (efekt == 'z'):
                        self.currentPawn = self.buttons[y][x]
                        if self.currentPawn['text'] == PLAYER_2_QUEEN:
                            self.currentPawn['text'] = PLAYER_2_QUEEN_SELECT
                        else:
                            self.currentPawn['text'] = PLAYER_2_SELECT
                        self.whitescore = self.whitescore + 1
                        self.update_score()
                        end(self.blackscore, self.whitescore)
                        return False
                    else:
                        self.currentPawn = None
                else:
                    return False
                return True

    def check_valid_move(self, yc, xc, yn, xn):
        enemy = ''
        enemyQueen = ''
        direction = 0
        isQueen = self.buttons[xc][yc]['text'] in (PLAYER_1_QUEEN_SELECT, PLAYER_2_QUEEN_SELECT)

        # player1
        if (self.state == 0 or self.state == 1):
            enemy = PLAYER_2
            enemyQueen = PLAYER_2_QUEEN
            direction = 1

        # player2
        if (self.state == 2 or self.state == 3):
            enemy = PLAYER_1
            enemyQueen = PLAYER_1_QUEEN
            direction = -1

        if isQueen:
            if abs(yn - yc) != abs(xn - xc):
                return False
            if abs(yn - yc) == 1:
                return 'p'
            dy = int(math.copysign(1, yn - yc))
            dx = int(math.copysign(1, xn - xc))
            zmienna = self.buttons[xn - dx][yn - dy]
            if (zmienna['text'] == enemy or zmienna['text'] == enemyQueen):
                for i in range(2, abs(yn - yc)):
                    y = yn - dy * i
                    x = xn - dx * i
                    if self.buttons[x][y]['text'] != '':
                        messagebox.showerror(title='Błąd', message='Ruch niedozwolony')
                        return False
                zmienna['text'] = ''
                return 'z'
            else:
                for i in range(1, abs(yn - yc)):
                    y = yn - dy * i
                    x = xn - dx * i
                    if self.buttons[x][y]['text'] != '':
                        messagebox.showerror(title='Błąd', message='Ruch niedozwolony')
                        return False
                return 'p'

        if (yn - yc == direction) and (xn - xc == 1):
            return 'p'
        if (yn - yc == direction) and (xn - xc == -1):
            return 'p'
        if (yn - yc == 2 * direction) and (xn - xc == 2):
            zmienna = self.buttons[xc + 1][yc + direction]
            if (zmienna['text'] == enemy or zmienna['text'] == enemyQueen):
                zmienna['text'] = ''
                return 'z'
            else:
                return False

        if (yn - yc == 2 * direction) and (xn - xc == - 2):
            zmienna = self.buttons[xc - 1][yc + direction]
            if (zmienna['text'] == enemy or zmienna['text'] == enemyQueen):
                zmienna['text'] = ''
                return 'z'
            else:
                return False
        messagebox.showerror(title='Błąd', message='Ruch niedozwolony')
        return False

    def player_turn(self):
        self.label.place(x=5, y=5, height=30, width=150)

    def change_player_turn(self):
        if (self.state == 0 or self.state == 1):
            self.label['text'] = 'Tura gracza 1'
        if (self.state == 2 or self.state == 3):
            self.label['text'] = 'Tura gracza 2'


def end(blackScore, whiteScore):
    if blackScore == 12:
        messagebox.showinfo(title='Koniec gry', message='Wygrał gracz 1!')
    elif whiteScore == 12:
        messagebox.showinfo(title='Koniec gry', message='Wygrał gracz 2!')


def main():
    root = tk.Tk()
    root.title("Warcaby")
    root.configure(bg='white')
    root.resizable(False, False)
    game = Game(root)

    root.mainloop()


if __name__ == "__main__":
    main()