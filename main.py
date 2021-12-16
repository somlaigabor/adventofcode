
# Advent of code day 2, first half

horizontal_position = 0
depth = 0


def slicing(data):
    direction = data[:-3]
    num = int(data[len(data)-2])
    return {"num": num, "direction": direction}


f = open("input.txt", "r")
for line in f:
    move = slicing(line)
    if move['direction'] == 'forward':
        horizontal_position += move['num']
    
    if move['direction'] == 'down':
        depth += move['num']

    if move['direction'] == 'up':
        depth -= move['num']
        
    dd = 2

print(horizontal_position*depth)
