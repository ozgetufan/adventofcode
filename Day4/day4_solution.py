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

print(splitted_list)
print(len(valid_test))


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

print(len(dict_list))

# Check four digits and eyr
for each_dict in dict_list:
    if len(str(each_dict['eyr'])) != 4 or len(str(each_dict['byr'])) != 4 or len(str(each_dict['iyr'])) != 4:
        dict_list.remove(each_dict)
    if each_dict['eyr'] < 2020 or each_dict['eyr'] > 2030:
        dict_list.remove(each_dict)

# Check byr
for each_dict in dict_list:
    if each_dict['byr'] < 1920 or each_dict['byr'] > 2002:
        dict_list.remove(each_dict)

# Check iyr
for each_dict in dict_list:
    if each_dict['iyr'] < 2010 or each_dict['iyr'] > 2020:
        dict_list.remove(each_dict)

print(dict_list)
# print(len(dict_list))

# Check hgt
for each_dict in dict_list:
    if len(each_dict['hgt']) == 5 or len(each_dict['hgt']) == 4:
        continue
    else:
        dict_list.remove(each_dict)

# Check hgt -- cm
for each_dict in dict_list:
    if len(each_dict['hgt']) == 5:
        if each_dict['hgt'][3] == 'c' and each_dict['hgt'][4] == 'm':
            if 149 < int(each_dict['hgt'][:3]) < 194:
                continue
            else:
                dict_list.remove(each_dict)
        else:
            dict_list.remove(each_dict)

# Check hgt -- inc
for each_dict in dict_list:
    if len(each_dict['hgt']) == 3:
        if each_dict['hgt'][2] == 'i' and each_dict['hgt'][3] == 'n':
            if 58 < int(each_dict['hgt'][:2]) < 77:
                continue
            else:
                dict_list.remove(each_dict)
        else:
            dict_list.remove(each_dict)


# Check hcl
for each_dict in dict_list:
    if each_dict['hcl'][0] == '#' and len(each_dict['hcl']) == 7:
        continue
    else:
        dict_list.remove(each_dict)


hcl_values = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for each_dict in dict_list:
    n = 0
    for x in each_dict['hcl'][1:]:
        if x not in hcl_values:
            n = n + 1
    if n != 0:
        dict_list.remove(each_dict)


print(len(dict_list))




