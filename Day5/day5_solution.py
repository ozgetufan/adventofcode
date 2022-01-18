with open('input_day5.txt') as f:
    lines = f.read().splitlines()

print(lines)

seat_ids = []
for line in lines:
    a = 0
    b = 127
    c = 0
    d = 7
    for x in line[:7]:
        if x == "F":
            b = a + (b-a)//2
        elif x == "B":
            a = a + (b-a)//2 + 1
    for y in line[7:10]:
        if y == "L":
            d = c + (d-c)//2
        if y == "R":
            c = c + (d-c)//2 + 1
    seat_id = (a * 8) + c
    seat_ids.append(seat_id)

print(max(seat_ids))






