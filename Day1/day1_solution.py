from itertools import combinations

with open('input.txt') as f:
    lines = f.read().splitlines()

values = []

for ele in lines:
    values.append(int(ele))

## Day 1 - Part 1
while len(values) > 0:
    for x in values[1:]:
        if x + values[0] == 2020:
            print(x * values[0])
    values.pop(0)

##Day 1 - Part 2

comb = combinations(values, 3)

for i in list(comb):
    if i[0] + i[1] + i[2] == 2020:
        print(i[0] * i[1] * i[2])






