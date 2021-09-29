with open('input_day4.txt') as f:
    lines = f.read().splitlines()

big_list = []
small_list = []
splitted_list = []
valid_test = []

print(lines[-1])
for i in range(len(lines)):
    if lines[i] != "":
        small_list.append(lines[i])
    else:
        big_list.append(small_list)
        small_list = []
else:
    big_list.append(small_list)
    small_list = []

print(big_list)
for ele in big_list:
    if len(ele) == 1:
        for x in ele:
            splitted = x.split(' ')
            splitted_list.append(splitted)
    else:
        joint = ' '.join(ele)
        sec_splitted = joint.split(' ')
        splitted_list.append(sec_splitted)

for x in splitted_list:
    if len(x) == 8:
        valid_test.append(1)
    elif len(x) == 7:
        a_list = []
        for i in x:
            if i[0] == 'c':  #if "cid" not in
                a_list.append(1)
        if len(a_list) == 0:
            valid_test.append(1)
    else:
        continue

valid_passports = 0
for x in splitted_list:
    if len(x) == 8:
        valid_passports += 1
    elif len(x) == 7:
        if all(["cid" not in field for field in x]):
            valid_passports += 1

print(splitted_list)
print(len(valid_test))
print(valid_passports)








