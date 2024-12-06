result = 0

with open('AdventOfCodeDay5/data5.txt', 'r') as file:
    data = file.read()

rules_raw, values_raw = data.split('\n\n')

rules = [list(map(int, line.split('|'))) for line in rules_raw.strip().splitlines()]
values = [list(map(int, line.split(','))) for line in values_raw.strip().splitlines()]

for value_set in values:

    all_rules_valid = True

    for rule in rules:
        if rule[0] in value_set and rule[1] in value_set:
            position_left = value_set.index(rule[0])
            position_right = value_set.index(rule[1])

            if position_left > position_right:
                all_rules_valid = False
                break

    if all_rules_valid:
        mid = len(value_set)//2
        result += value_set[mid]

print(result)