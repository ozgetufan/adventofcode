with open('input_day3.txt') as f:
    lines = f.read().splitlines()



new_lines = []
root_list = []  # use this list
trees = []
p2_t1 = []

for all_ele in lines:
    new_str = "".join((all_ele,)*100)
    new_lines.append(new_str)


for ele in new_lines:
    child_list = []
    child_list.append(ele)
    root_list.append(child_list)

#Part1
x = 3
for i in range(1, len(root_list)):
    if root_list[i][0][x] == "#":
        trees.append(1)
    x = x + 3
    if i == len(root_list)-1:
        if root_list[i][0][x] == "#":
            trees.append(1)



#Part2
# y1 = 7
# for i in range(1, len(root_list)):
#     if root_list[i][0][y1] == "#":
#         p2_t1.append(1)
#     y1 = y1 + 7
#     if i == len(root_list)-1:
#         if root_list[i][0][y1] == "#":
#             p2_t1.append(1)
#
# print(len(p2_t1))

# y2 = 7
# for i in range(1, len(root_list)):
#     if root_list[i][0][y2] == "#":
#         p2_t1.append(1)
#     y2 = y2 + 3
#     if i == len(root_list)-1:
#         if root_list[i][0][y2] == "#":
#             p2_t1.append(1)
#
# print(len(p2_t1))

y2 = 1
for i in range(1, len(root_list)):
    if i%2 == 0:
        if root_list[i][0][y2] == "#":
            p2_t1.append(1)
        y2 = y2 + 1
        if i == len(root_list)-1:
            if root_list[i][0][y2] == "#":
                p2_t1.append(1)

print(len(p2_t1))
#
print(79*234*72*91*48)








