### DAY 5 ###
import re

with open('data.txt') as file:
    game = [x.strip().replace('    ', ' 0').replace('[', '').replace(']', '') for x in file]
checks = [[x.replace(' ', '') for x in x if x != ' '] for x in game[0:8] if x]
new_list = []
temp_list = []
for x in range(len(checks)+1):
    for y in range(len(checks)):
        temp_list.append(checks[y][x]) 
    p = ''.join(temp_list)
    new_list.append(p)
    temp_list.clear()
new_list = [x.replace('0', '') for x in new_list]
for m in game[10:]:
    checking_regex = re.findall(r'[\d]+', m)
    # Assignment 1
    for a in range(int(checking_regex[0])):
        v = new_list[int(checking_regex[1])-1][0]
        new_list[int(checking_regex[1])-1] = new_list[int(checking_regex[1])-1].replace(v, '', 1)
        new_list[int(checking_regex[2])-1] = v + new_list[int(checking_regex[2])-1]
    # Assignment 2
    v = new_list[int(checking_regex[1]) - 1][:int(checking_regex[0])]
    new_list[int(checking_regex[1])-1] = new_list[int(checking_regex[1])-1].replace(v, '', 1)
    new_list[int(checking_regex[2])-1] = v + new_list[int(checking_regex[2])-1]

print(new_list)
