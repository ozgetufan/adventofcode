with open('input_day4.txt') as f:
    lines = f.read().splitlines()

big_list = []
small_list = []
splitted_list = []
valid_test = []
valid_pass = []

# Part 1
for i in range(len(lines)):
    if lines[i] != "":
        small_list.append(lines[i])
    else:
        big_list.append(small_list)
        small_list = []
else:
    big_list.append(small_list)
    small_list = []

# print(big_list)
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
        valid_pass.append(x)
    elif len(x) == 7:
        a_list = []
        for i in x:
            if i[0] == 'c':  #if "cid" not in
                a_list.append(1)
        if len(a_list) == 0:
            valid_test.append(1)
            valid_pass.append(x)
    else:
        continue
# # Matteo's solution
# valid_passports = 0
# for x in splitted_list:
#     if len(x) == 8:
#         valid_passports += 1
#     elif len(x) == 7:
#         if all(["cid" not in field for field in x]):
#             valid_passports += 1

# print(splitted_list)
# print(len(valid_test))


#Part 2
dict_list = []
for x in valid_pass:
    my_dict = {}
    for each in x:
        a, b = each.split(':')
        my_dict[a] = b
    dict_list.append(my_dict)

for each_dict in dict_list:
    for x in each_dict.keys():
        if x == 'eyr' or x == 'byr' or x == 'iyr': #pid cannot be add because there is a 161cm value somewhere!!.
            each_dict[x] = int(each_dict.get(x)) #set the values to integer

invalid_list = []
# Check eyr
for each_dict in dict_list:
    if each_dict['eyr'] < 2020 or each_dict['eyr'] > 2030:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)
# Check byr
for each_dict in dict_list:
    if each_dict['byr'] < 1920 or each_dict['byr'] > 2002:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)

# Check iyr
for each_dict in dict_list:
    if each_dict['iyr'] < 2010 or each_dict['iyr'] > 2020:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)

# Check hgt
for each_dict in dict_list:
    if len(each_dict['hgt']) == 5 or len(each_dict['hgt']) == 4:
        continue
    else:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)

for each_dict in dict_list:
    if each_dict['hgt'][-2:] == 'cm':
        if 149 < int(each_dict['hgt'][:-2]) < 194:
            continue
        else:
            if each_dict not in invalid_list:
                invalid_list.append(each_dict)
    elif each_dict['hgt'][-2:] == 'in':
        if 58 < int(each_dict['hgt'][:-2]) < 77:
            continue
        else:
            if each_dict not in invalid_list:
                invalid_list.append(each_dict)
    else:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)


# Check hcl
for each_dict in dict_list:
    if each_dict['hcl'][0] == '#' and len(each_dict['hcl']) == 7:
        continue
    else:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)

hcl_values = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for each_dict in dict_list:
    for x in each_dict['hcl'][1:]:
        if x not in hcl_values:
            if each_dict not in invalid_list:
                invalid_list.append(each_dict)
            break

# Check ecl
ecl_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for each_dict in dict_list:
    if len(each_dict['ecl']) != 3:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)
for each_dict in dict_list:
    if each_dict['ecl'] not in ecl_values:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)

# Check pid
for each_dict in dict_list:
    if len(each_dict['pid']) != 9:

        if each_dict not in invalid_list:
            invalid_list.append(each_dict)
for each_dict in dict_list:
    try:
        int(each_dict['pid'])
    except ValueError:
        if each_dict not in invalid_list:
            invalid_list.append(each_dict)

print(len(dict_list) - len(invalid_list))




