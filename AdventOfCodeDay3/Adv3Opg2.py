import re

result = 0
dos = True

with open("AdventOfCodeDay3/data3.txt", "r") as file:
    content = file.read()

instructions = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", content)

for instruction in instructions:
    if instruction == "do()":
        dos = True
    elif instruction == "don't()":
        dos = False
    elif dos: 
        match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
        if match:
            num1, num2 = int(match[1]), int(match[2])
            result += num1 * num2
print(result)
