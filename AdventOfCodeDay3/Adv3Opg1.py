import re

result = 0

with open("AdventOfCodeDay3/data3.txt", "r") as file:
    content = file.read()

matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", content)

for match in matches:
    num1, num2 = int(match[0]), int(match[1])
    if match:
        temp = num1 * num2
        result += temp

print(result)
