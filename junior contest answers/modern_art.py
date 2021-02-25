rows = int(input())
columns = int(input())

num_choices = int(input())
choices = []
for i in range(num_choices):
    choices.append(input())

colours = []
for row in range(rows):
    colours_row = []
    for column in range(columns):
        colours_row.append('B')
    colours.append(colours_row)

gold_amount = 0

for i in choices:
    rc, num = i.split()
    num = int(num)
    if rc == 'R':
        count = 0
        for item in colours[num-1]:
            if item == 'B':
                colours[num-1][count] = 'G'
                #colours[num-1][(colours[num-1].index(item))] = 'G'
                gold_amount += 1
            elif item == 'G':
                colours[num-1][count] = 'B'
                #colours[num-1][(colours[num-1].index(item))] = 'B'
                gold_amount -= 1
            count += 1
        
    elif rc == 'C':
        for row in colours:
            if row[num-1] == 'B':
                colours[colours.index(row)][num-1] = 'G'
                gold_amount += 1
            elif row[num-1] == 'G':
                colours[colours.index(row)][num-1] = 'B'
                gold_amount -= 1
print(gold_amount)
