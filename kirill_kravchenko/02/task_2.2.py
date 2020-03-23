# Reverse a string
#
# Examples:
#
# input: "Hello"
# output: "olleH"

# ======
# 1 variant
# ======

str_reverse = list(input("Input string for reverse "))

new_list = []
key = 0

for j in str_reverse:

    key += 1
    new_list.append(str_reverse[-key])

for let in new_list:
    print(let, end='')

print("\n")

# ======
# 2 variant
# ======

str_reverse = list(input("Input string for reverse "))

new_list = []

for i in range(1, len(str_reverse)):
    new_list.append(str_reverse[-i])

new_list.append(str_reverse[0])

for let in new_list:
    print(let, end='')

print("\n")


# ======
# 3 variant
# ======

str_reverse = list(input("Input string for reverse "))

new_list = []

for i in range(len(str_reverse) - 1, -1, -1):
    new_list.append(str_reverse[i])

for let in new_list:
    print(let, end='')

print("\n")

# ======
# 4 variant
# Not in class
# ======

str_reverse = list(input("Input string for reverse "))

for let in reversed(str_reverse):
    print(let, end='')