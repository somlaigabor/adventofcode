
# Advent of code day 1, first half
numbers = 0
k = None
f = open("input.txt", "r")
for line in f:
    if k:
        if int(k) < int(line):
            numbers += 1
    k = int(line)

print(numbers)

# # Advent of code day 1, second half
# window = []
# actual_window_size = 3
#
#
# def sliding_window(array, new_item, window_size):
#     array.append(new_item)
#     if len(array) > window_size:
#         array.pop(0)
#     return array
#
#
# def a_sum(arr):
#     array_sum = 0
#     for i in arr:
#         array_sum = array_sum + i
#
#     return array_sum
#
# numbers = 0
# k = None
# f = open("input.txt", "r")
# for line in f:
#     window = sliding_window(window, int(line), actual_window_size)
#     if len(window) > 2:
#         if k:
#             if int(k) < a_sum(window):
#                 numbers += 1
#         k = a_sum(window)
#
# print(numbers)

