from itertools import product

def check_combinations():
    result = {}
    
    with open("AdventOfCodeDay7/data7.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                key, values = line.split(":")
                key = int(key.strip())
                values = list(map(int, values.split()))
                result[key] = values

    total_sum = 0
    
    for test_value, numbers in result.items():
        n = len(numbers)
        if n < 2:
            continue

        operator_combinations = product(['+', '*'], repeat=n-1)

        for operators in operator_combinations:
            expr = numbers[0]
            for i in range(1, n):
                if operators[i-1] == '+':
                    expr += numbers[i]
                elif operators[i-1] == '*':
                    expr *= numbers[i]

            if expr == test_value:
                total_sum += test_value
                break

    print("Total calibration result:", total_sum)

check_combinations()
