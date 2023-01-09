### DAY 4 ###
with open('data.txt') as file:
    game = [x.strip() for x in file]

sum = 0

for x in game:
    orders = x.split(',')
    for values in range(len(orders)):
        if values != len(orders)-1:
            a = orders[values]
        else:
            b = orders[values]
            checking1 = a.split('-')
            checking2 = b.split('-')
            # 1st assignment
            if (int(checking1[0]) <= int(checking2[0]) and int(checking1[1]) >= int(checking2[1])) or (int(checking2[0]) <= int(checking1[0]) and int(checking2[1]) >= int(checking1[1])):
                sum+= 1
            # 2nd assignment
            if (int(checking1[0]) <= int(checking2[1]) and int(checking2[0]) <= int(checking1[1])):
                sum+= 1
print(sum) 
