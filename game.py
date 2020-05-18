import tkinter as tk

class Board():
    def __init__(self, parent, rows = 8, columns = 8, color1 = 'white', color2 = 'black', size = 64):
        self.rows = rows
        self.columns = columns
        self.color1 = color1
        self.color2 = color2
        self.size = size
        self.parent = parent

        canvas_width = self.columns * self.size
        canvas_height = self.rows * self.size
        self.border_size = 3

        self.turncanvas = tk.Canvas(parent, width=150, height=30, background='grey', borderwidth=self.border_size, relief='solid', highlightbackground='grey')
        self.label = tk.Label(self.turncanvas, text='Tura gracza 1')
        self.change_player_turn()
        self.turncanvas.pack()
        self.player_turn()

        self.canvas = tk.Canvas(parent, width=canvas_width, height=canvas_height, background='grey', borderwidth=self.border_size, relief='solid', highlightbackground='grey')
        self.canvas.pack()
        self.draw_board()

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

    def player_turn(self):
        self.label.place(x=5, y=5 ,height=30, width=150)

    def change_player_turn(self):
        if self.label['text'] == 'Tura gracza 1':
            self.label['text'] = 'Tura gracza 2'
        else:
            self.label['text'] = 'Tura gracza 1'

def main():
    root = tk.Tk()
    root.title("Warcaby")
    root.configure(bg='grey')
    root.resizable(False, False)
    board = Board(root)

    root.mainloop()

if __name__ == "__main__":
    main()