result = 0
def x_mas(char_2d_array, x, y):
    try:
            return [
                char_2d_array[y][x],
                char_2d_array[y + 1][x + 1],
                char_2d_array[y + 2][x + 2],
                char_2d_array[y][x + 2],
                char_2d_array[y + 2][x]
            ]
    except IndexError:
        return None
    
with open("AdventOfCodeDay4/data4.txt", "r") as file:
    char_2d_array = [list(line.strip()) for line in file if line.strip()]   

for y in range(len(char_2d_array)):
    for x in range(len(char_2d_array[y])):
        x_mas_result = x_mas(char_2d_array, x, y)
        if x_mas_result == ['M', 'A', 'S', 'M', 'S'] or x_mas_result == ['S', 'A', 'M', 'S', 'M'] or x_mas_result == ['M', 'A', 'S', 'S', 'M'] or x_mas_result == ['S', 'A', 'M', 'M', 'S']:
            result += 1
        
print(result)