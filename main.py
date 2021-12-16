
# Advent of code day 2, second half

line_numbers = 0
len_of_numbers = 0
sum_of_items = [None]
frequent_nums = [None]
unfrequent_nums = [None]

def split(word):
    return [char for char in word]


f = open("input.txt", "r")
for line in f:
    if len_of_numbers == 0:
        len_of_numbers = len(line)
        sum_of_items = [0] * int(len_of_numbers-1)
        frequent_nums = [0] * int(len_of_numbers-1)
        unfrequent_nums = [0] * int(len_of_numbers-1)
        
    if sum_of_items:
        numbers_list = split(line)
        for number in range(0, len_of_numbers-1):
            sum_of_items[number]+=int(numbers_list[number])
        line_numbers += 1

print(sum_of_items)
print(line_numbers)

for number in range(0, len_of_numbers-1):
    z = line_numbers//2
    if sum_of_items[number] > line_numbers//2:
        frequent_nums[number] = 1
        unfrequent_nums[number] = 0
    else:
        frequent_nums[number] = 0
        unfrequent_nums[number] = 1

frequent_nums_dec = int(''.join(str(i) for i in frequent_nums),2)
unfrequent_nums_dec = int(''.join(str(i) for i in unfrequent_nums),2)
print(frequent_nums_dec)
print(unfrequent_nums_dec)
print(unfrequent_nums_dec*frequent_nums_dec)
