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
    if left_array[i] > right_array[i]:
       temp = left_array[i] - right_array[i]
       result = temp + result
    else:
       temp = right_array[i] - left_array[i]
       result = temp + result

print(result)