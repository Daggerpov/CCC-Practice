secret_instructions = []

current = 0

directions = []

while True:
    instruction = input()

    if instruction == '99999':
        break
    sum = int(instruction[0]) + int(instruction[1])

    if sum % 2 == 0 and sum != 0:
        direction = 'right '
    elif sum % 2 == 1:
        direction = 'left '
    else:
        direction = directions[current-1]
    
    directions.append(direction)

    instruction = direction + instruction[2:]
    
    secret_instructions.append(instruction)

    current += 1
for instruction in secret_instructions:
    print(instruction)