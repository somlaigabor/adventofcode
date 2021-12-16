
# Advent of code day 3, second half

line_numbers = 0
len_of_numbers = 0
oxygen_nums = []
co2_nums = []
oxygen_nums_remove = []
co2_nums_remove = []

def split(word):
    return [char for char in word]


def splittoint(word):
    a_list = split(word)
    map_object = map(int, a_list)
    list_of_integers = list(map_object)
    return list_of_integers


f = open("input.txt", "r")
for line in f:
    if len_of_numbers == 0:
        len_of_numbers = len(line)
        sum_of_oxygenitems = [0] * int(len_of_numbers-1)
        sum_of_co2items = [0] * int(len_of_numbers-1)
        frequent_nums = [0] * int(len_of_numbers-1)
        unfrequent_nums = [0] * int(len_of_numbers-1)

    numbers_list = splittoint(line[:-1])
    oxygen_nums.append(numbers_list)
    co2_nums.append(numbers_list)
    line_numbers += 1


for number in range(0, len_of_numbers-1):
    for item in oxygen_nums:
        sum_of_oxygenitems[number] += int(item[number])
    if sum_of_oxygenitems[number] >= len(oxygen_nums)/2:
        frequent_nums[number] = 1
    else:
        frequent_nums[number] = 0

    for numb in oxygen_nums:
        if numb[number] != frequent_nums[number]:
            oxygen_nums_remove.append(numb)

    for deleted in oxygen_nums_remove:
        if len(oxygen_nums) == 1:
            break
        oxygen_nums.remove(deleted)
    oxygen_nums_remove = []

for number in range(0, len_of_numbers-1):
    for item in co2_nums:
        sum_of_co2items[number] += int(item[number])
    if sum_of_co2items[number] >= len(co2_nums)/2:
        unfrequent_nums[number] = 0
    else:
        unfrequent_nums[number] = 1
    for numb in co2_nums:
        if numb[number] != unfrequent_nums[number]:
            co2_nums_remove.append(numb)

    for deleted in co2_nums_remove:
        if len(co2_nums) == 1:
            break
        co2_nums.remove(deleted)
    co2_nums_remove = []

oxygen_nums_dec = int(''.join(str(i) for i in oxygen_nums[0]), 2)
co2_nums_dec = int(''.join(str(i) for i in co2_nums[0]), 2)
print(oxygen_nums_dec)
print(co2_nums_dec)
print(oxygen_nums_dec*co2_nums_dec)
