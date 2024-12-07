import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def find_start_pos():
    for row_index, row in enumerate(char_2d_array):
        for col_index, char in enumerate(row):
            if char == '^':
                return row_index, col_index
    return None

def check_index(y, x):
    if y < 0 or x < 0:
        raise IndexError("Index went out of bounds: Negative index detected")


def movement(y, x):
    print(f'Start postition is y = {y}, x = {x}')
    try:
        while True:
            up = True
            right = False
            down = False
            left = False
            if up:
                while True:
                    check_index(y - 1, x)
                    char_2d_array[y][x] = 'x'
                    y -= 1
                    if char_2d_array[y - 1][x] == '#':
                        up = False
                        right = True
                        break
            if right:
                while True:
                    char_2d_array[y][x] = 'x'
                    x += 1
                    if char_2d_array[y][x + 1] == '#':
                        right = False
                        down = True
                        break
            if down:
                while True:
                    char_2d_array[y][x] = 'x'
                    y += 1
                    if char_2d_array[y + 1][x] == '#':
                        down = False
                        left = True
                        break
            if left:
                while True:
                    check_index(y, x - 1)
                    char_2d_array[y][x] = 'x'
                    x -= 1
                    if char_2d_array[y][x - 1] == '#':
                        left = False
                        up = True
                        break
    except IndexError:
        char_2d_array[y][x] = 'x'
        return None
    
def count_x():
    xes = 0
    for row_index, row in enumerate(char_2d_array):
        for col_index, char in enumerate(row):
            if char == 'x':
                xes += 1
    return print(xes)

with open("AdventOfCodeDay6/data6.txt", "r") as file:
    char_2d_array = [list(line.strip()) for line in file if line.strip()]

start_row, start_col = find_start_pos()
movement(start_row, start_col)

for line in char_2d_array:
    print(''.join(Fore.RED + char + Style.RESET_ALL if char == 'x' else char for char in line))

count_x()