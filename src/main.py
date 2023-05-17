from graphics import Window
# from maze import Maze
import sys


def main():
    num_rows = 3
    num_cols = 3
    margin = 100
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window()

    win.draw_button()
    # # maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    # print("maze created")
    # is_solveable = maze.solve()
    # if not is_solveable:
    #     print("maze can not be solved!")
    # else:
    #     print("maze solved!")
    win.wait_for_close()


main()