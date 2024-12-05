result = 0

def vertical(char_2d_array, x, y):
    try:
        return [
            char_2d_array[y][x],
            char_2d_array[y + 1][x],
            char_2d_array[y + 2][x],
            char_2d_array[y + 3][x]
        ]
    except IndexError:
        return None
    
def horizontal(char_2d_array, x, y):
    try:
        return [
            char_2d_array[y][x],
            char_2d_array[y][x + 1],
            char_2d_array[y][x + 2],
            char_2d_array[y][x + 3]
        ]
    except IndexError:
        return None
    
def diagonal_down_right(char_2d_array, x, y):
    try:
        return [
            char_2d_array[y][x],
            char_2d_array[y + 1][x + 1],
            char_2d_array[y + 2][x + 2],
            char_2d_array[y + 3][x + 3]
        ]
    except IndexError:
        return None

def diagonal_down_left(char_2d_array, x, y):
    try:
        if x >= 3:
            return [
                char_2d_array[y][x],
                char_2d_array[y + 1][x - 1],
                char_2d_array[y + 2][x - 2],
                char_2d_array[y + 3][x - 3]
            ]
    except IndexError:
        return None

with open("AdventOfCodeDay4/data4.txt", "r") as file:
    char_2d_array = [list(line.strip()) for line in file if line.strip()]   

for y in range(len(char_2d_array)):
    for x in range(len(char_2d_array[y])):
        vertical_result = vertical(char_2d_array, x, y)
        if vertical_result == ['X', 'M', 'A', 'S'] or vertical_result == ['S', 'A', 'M', 'X']:
            result += 1
        
        horizontal_result = horizontal(char_2d_array, x, y)
        if horizontal_result == ['X', 'M', 'A', 'S'] or horizontal_result == ['S', 'A', 'M', 'X']:
            result += 1

        diagonal_down_right_result = diagonal_down_right(char_2d_array, x, y)
        if diagonal_down_right_result == ['X', 'M', 'A', 'S'] or diagonal_down_right_result == ['S', 'A', 'M', 'X']:
            result += 1

        diagonal_down_left_result = diagonal_down_left(char_2d_array, x, y)
        if diagonal_down_left_result == ['X', 'M', 'A', 'S'] or diagonal_down_left_result == ['S', 'A', 'M', 'X']:
            result += 1

print(result)