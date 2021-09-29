with open('input_day2.txt') as f:
    lines = f.read().splitlines()

#Part 1
m_list = []

for ele in lines:
    splitted = ele.split(' ')
    condition = splitted[0].split('-')
    letter = splitted[1]
    password = splitted[2]
    counted = password.count(letter[0])

    if int(condition[0]) <= counted <= int(condition[1]):
        m_list.append(1)

print(len(m_list))

#Part 2
new_list = []
for ele in lines:
    splitted = ele.split(' ')
    condition = splitted[0].split('-')
    letter = splitted[1]
    password = splitted[2]
    if (password[int(condition[0])-1] == letter[0] and password[int(condition[1])-1] != letter[0]) or (password[int(condition[1])-1] == letter[0] and password[int(condition[0])-1] != letter[0]):
        new_list.append(1)

print(len(new_list))


