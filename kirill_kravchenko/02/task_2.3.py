# Given an array, find the int that appears an odd number of times. There will always be only one integer that appears an odd number of times.
#
# Examples:
#
# list: [1, 2, 3, 1, 3, 2, 1]
# output: 1

str = [1, 2, 3, 1, 3, 2, 1]

# ======
# 1 variant
# ======

for i in str:

    equiv = 0

    for j in str:

        if i == j:
            equiv += 1

    if equiv > 1 and equiv % 2:
        print(f'This is number "{i}" occurs "{equiv}" times in array')
        break

if equiv == 0:
    print(f'There is no number that occurs odd times in array')

# ======
# 2 variant, not optimal, not normal, but all numbers
# ======

str_odd = []

for i in str:

    str_odd.append([i for j in str if i == j])

for j in str_odd:

    length = len(j)
    if length > 1 and length % 2:
        print(f'This is number "{j[0]}" occurs "{length}" times in array')
        break

# ======
# 3 variant
# ======

new_array = []
new_index_array = []

for i in str:

    flag = True
    for j in range(len(new_array)):
        if new_array[j] == i:
            new_index_array[j] += 1
            flag = False

    if flag:
        new_array.append(i)
        new_index_array.append(1)

for j in range(len(new_index_array)):
    if new_index_array[j] % 2:
        print(f'This is number "{new_array[j]}" occurs "{new_index_array[j]}" times in array')
        break
