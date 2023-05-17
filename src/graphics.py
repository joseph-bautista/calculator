from tkinter import * 
from tkinter import messagebox


class Window:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Tic Tac Toe")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__running = False
        self.b = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.__states = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.__player = 'X'
        self.__stop_game = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def button_clicked(self, r, c):
        if(self.__player == "X" and self.__states[r][c] == 0 and self.__stop_game == False):
            self.b[r][c].configure(text="X")
            self.__states[r][c] = 'X'
            self.__player = 'O'
        if(self.__player == "O" and self.__states[r][c] == 0 and self.__stop_game == False):
            self.b[r][c].configure(text="O")
            self.__states[r][c] = 'O'
            self.__player = 'X'
        
        self.check_if_win()

    def draw_button(self):
        for i in range(3):
            for j in range(3):
                self.b[i][j] = Button(height=4, width=8, font=("Helvetica", "20"), command = lambda r=i , c=j: self.button_clicked(r,c))
                self.b[i][j].grid(row=i,column=j)

    def check_if_win(self):
        for i in range(3):
            if self.__states[i][0] == self.__states[i][1] == self.__states[i][2] !=0:
                self.__stop_game = True
    
                winner = messagebox.showinfo("Winner", self.__states[i][0] + " Won")
                # disableAllButton()
                break
    
        # for j in range(3):
            elif self.__states [0][i] == self.__states[1][i] == self.__states[2][i] != 0:
                self.__stop_game = True
    
                winner = messagebox.showinfo("Winner", self.__states[0][i]+ " Won!")
                break
    
            elif self.__states[0][0] == self.__states[1][1] == self.__states[2][2] !=0:
                self.__stop_game = True
    
                winner = messagebox.showinfo("Winner", self.__states[0][0]+ " Won!")
                break
    
            elif self.__states[0][2] == self.__states[1][1] == self.__states[2][0] !=0:
                self.__stop_game = True
    
                winner = messagebox.showinfo("Winner" , self.__states[0][2]+ " Won!")
                break
    
            elif self.__states[0][0] and self.__states[0][1] and self.__states[0][2] and self.__states[1][0] and self.__states[1][1] and self.__states[1][2] and self.__states[2][0] and self.__states[2][1] and self.__states[2][2] != 0:
                self.__stop_game = True
 
                winner = messagebox.showinfo("tie", "Tie")

    def close(self):
        self.__running = False

