numbers = [1, 2, 3, 4, 5]
new_list = []

for num in numbers:
    if num % 2 == 1:  # თუ კენტია
        new_list.append(num * 2)

print(new_list)  # [2, 6, 10]



new_list = [num * 2 for num in [1, 2, 3, 4, 5] if num % 2 == 1]
print(new_list)  # [2, 6, 10]






nums = [1, 2, 3]
new_list = [x + 5 for x in nums]
print(new_list)  # [6, 7, 8]




nums = [1, 2, 3, 4]
new_list = [x for x in nums if x % 2 == 0]
print(new_list)  # [2, 4]
