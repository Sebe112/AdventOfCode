result = 0

with open('AdventOfCodeDay5/data5.txt', 'r') as file:
    data = file.read()

rules_raw, values_raw = data.split('\n\n')

rules = [list(map(int, line.split('|'))) for line in rules_raw.strip().splitlines()]
values = [list(map(int, line.split(','))) for line in values_raw.strip().splitlines()]

for value_set in values:

    initially_correct = True

    for rule in rules:
        if rule[0] in value_set and rule[1] in value_set:
            if value_set.index(rule[0]) > value_set.index(rule[1]):
                initially_correct = False
                break

    if not initially_correct:
        changed = True
        while changed:
            changed = False
            for rule in rules:
                if rule[0] in value_set and rule[1] in value_set:
                    if value_set.index(rule[0]) > value_set.index(rule[1]):
                        value_set.remove(rule[1])
                        value_set.insert(value_set.index(rule[0]) + 1, rule[1])
                        changed = True

        result += value_set[len(value_set) // 2]

print(result)