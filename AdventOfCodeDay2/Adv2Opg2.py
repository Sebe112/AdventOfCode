result = 0
counter = 0

with open("AdventOfCodeDay2/data2.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))

        if all(1 <= (numbers[i] - numbers[i - 1]) <= 3 for i in range(1, len(numbers))) or \
        all(-3 <= (numbers[i] - numbers[i - 1]) <= -1 for i in range(1, len(numbers))):
            result += 1

        else:
            for counter in range(len(numbers)):
                modified_numbers = numbers[:counter] + numbers[counter + 1:]
                if all(1 <= (modified_numbers[i] - modified_numbers[i - 1]) <= 3 for i in range(1, len(modified_numbers))) or \
                   all(-3 <= (modified_numbers[i] - modified_numbers[i - 1]) <= -1 for i in range(1, len(modified_numbers))):
                    result += 1
                    break
                
print(result)