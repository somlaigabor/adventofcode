
# Advent of code day 2, second half

horizontal_position = 0
depth = 0
depth_aim = 0

def slicing(data):
    direction = data[:-3]
    num = int(data[len(data)-2])
    return {"num": num, "direction": direction}


f = open("input.txt", "r")
for line in f:
    move = slicing(line)
    if move['direction'] == 'forward':
        horizontal_position += move['num']
        depth += depth_aim*move['num']
    
    if move['direction'] == 'down':
        depth_aim += move['num']

    if move['direction'] == 'up':
        depth_aim -= move['num']

print(horizontal_position*depth)
