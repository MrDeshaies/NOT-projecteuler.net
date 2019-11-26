# Simple Tic-Tac-Toe games for the kids... Allô Rom et Adri!
import random
BLANK = ' '
def print_grid(grid):
    print(" {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} ".format(\
        grid[0],grid[1],grid[2],grid[3],grid[4],grid[5],grid[6],grid[7],grid[8]))

def get_move(grid):
    while True:
        try:
            x = int(input("Enter position [1-9]: "))
            if grid[x-1] == BLANK:
                grid[x-1] = 'X'
                return
        except:
            pass

def play_computer_O(grid):
    while True:
        o = random.randint(0,8)
        if grid[o] == BLANK:
            grid[o] = 'O'
            return

def check_win(grid,symbol):
    win_positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    if symbol*3 in [''.join([grid[p[0]],grid[p[1]],grid[p[2]]]) for p in win_positions]:
        print_grid(grid)
        print(symbol," wins!")
        exit(0)

grid = [BLANK for i in range(9)]
print_grid(range(1,10))
while True:
    get_move(grid)
    check_win(grid, 'X')
    play_computer_O(grid)
    check_win(grid, 'O')
    print_grid(grid)