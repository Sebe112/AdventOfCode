result = 0

with open("AdventOfCodeDay2/data2.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if all(1 <= (numbers[i] - numbers[i - 1]) <= 3 for i in range(1, len(numbers))) or \
        all(-3 <= (numbers[i] - numbers[i - 1]) <= -1 for i in range(1, len(numbers))):
            result += 1

print(result)