temp = int()
result = int()

with open("AdventOfCodeDay1/data1.txt", "r") as file:
    data = file.readlines()

left_array = []
right_array = []

for line in data:
    left, right = line.split()
    left_array.append(int(left))
    right_array.append(int(right))

left_array.sort()
right_array.sort()

for i in range(len(left_array)):
    temp = 0
    for j in range(len(right_array)):
        if left_array[i] == right_array[j]:
            temp += 1
        if j == len(right_array)-1 and temp != 0:
            result += left_array[i] * temp

print(result)