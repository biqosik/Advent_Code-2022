### DAY 3 ###
with open('data.txt') as file:
    game = [x.strip() for x in file]


sums = 0

for x in range(0,len(game),3):
    a = set(game[x])
    b = set(game[x+1])
    c = set(game[x+2])
    h = a&b&c
    for x in h:
        if len(x) == 0:
            pass
        else:
            if x.isupper():
                sums += ord(x) - 38
            elif x.islower():
                sums += ord(x) - 96

for x in game:
    z = set(x[:len(x) // 2])
    y = set(x[len(x) // 2:])
    h = y & z
    for x in h:
        if len(x) == 0:
            pass
        else:
            if x.isupper():
                sums += ord(x) - 38
            elif x.islower():
                sums += ord(x) - 96

print(sums)
