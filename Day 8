### DAY 8 ###
import numpy as np

with open('data.csv') as file:
    digits = [[x.strip() for x in x if x.strip()] for x in file]

array_x = np.array(digits)
array_y = np.swapaxes(array_x, 0, 1)
maxes = 0
sums = (2 * len(array_x)) + (2 * len(array_y) - 4)
for count, value in enumerate(array_x):
    if count == 0 or count == len(array_x)-1:
        continue
    for values in range(1, len(value)-1):
        #Assignment 2
        try:
            if (int(max(np.argwhere(value[:values] >= value[values])))) > 0:
                max_1 = values - int(max(np.argwhere(value[:values] >= value[values])))
        except:
            max_1 = len(value[:values])
        finally:
            try:
                if (int(min(np.argwhere(value[values + 1:] >= value[values])))):
                    max_2 = int(min(np.argwhere(value[values + 1:] >= value[values]))) + 1
            except:
                max_2 = len(value[values + 1:])
            finally:
                try:
                    if (int(min(np.argwhere(array_y[values][count + 1:] >= value[values])))) is not None:
                        max_3 = int(min(np.argwhere(array_y[values][count + 1:] >= value[values]))) + 1
                except:
                    max_3 = len(array_y[values][count + 1:])                   
                finally:
                    try:
                        if (int(max(np.argwhere(array_y[values][:count] >= value[values])))) > 0:
                            max_4 = count - int(max(np.argwhere(array_y[values][:count] >= value[values])))
                    except:
                        max_4 = len(array_y[values][:count])
                    finally:
                        if max_1 * max_2 * max_3 * max_4 > maxes:
                            maxes = max_1 * max_2 * max_3 * max_4
                            saves_those_values = [max_1, max_2, max_3, max_4,count, value,values, value[values]]
         #Assignment 1
        if max(value[:values]) < value[values] or max(value[values + 1:]) < value[values] or max(array_y[values][count + 1:]) < value[values] or max(array_y[values][:count]) < value[values]:
            sums += 1
print(sums)
print(maxes)
print(saves_those_values)
