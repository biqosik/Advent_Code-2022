### DAY 1 ###

with open('data.txt') as file:
    digits = [x.strip() for x in file]
tempvalue = 0
additional_digits = []
final_value = 0
for x in digits:
    if len(x) != 0:
        tempvalue += int(x)
        if tempvalue > final_value:
            final_value=tempvalue
    else:
        additional_digits.append(tempvalue)
        tempvalue = 0
for x in range(3):
    print(max(additional_digits))
    additional_digits.remove(max(additional_digits))
