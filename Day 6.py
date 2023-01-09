### DAY 6 ###
with open('data.txt') as file:
    x = file.readline()
index = 14 # or 4
for f in range(len(x)):
    checking = set(x[f:index:])
    if len(checking) == 14: # or 4
        break
    index+=1
print(index)
