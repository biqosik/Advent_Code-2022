### DAY 2 ###

# A = X = Rock /// Lose
# B = Y = Paper /// Draw
# C = Z = Scissors /// Win
with open('data.txt') as file:
    game = [x.strip() for x in file]
dict_values_game1 = { 'A Y' : 8,
                'B Z' : 9,
                'C X' : 7,
                'A X' : 4,
                'B Y' : 5,
                'C Z' : 6,
                'A Z' : 3,
                'B X' : 1,
                'C Y' : 2,}
dict_values_game2 = { 'A Y' : 4,
                'B Z' : 9,
                'C X' : 2,
                'A X' : 3,
                'B Y' : 5,
                'C Z' : 7,
                'A Z' : 8,
                'B X' : 1,
                'C Y' : 6,}
                

final_value = 0
for x in game:
    if x in dict_values_game2:
        final_value += dict_values_game2.get(x)

for x in game:
    if x in dict_values_game1:
        final_value += dict_values_game1.get(x)

print(final_value)
