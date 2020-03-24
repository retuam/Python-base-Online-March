# Check to see if a string has the same amount of 'x's and 'o's. The string can contain any char.
#
# Examples:
#
# input: "ooxx"
# output: True
#
# input: "xooxx"
# output: False
#
# input: "ooxXm"
# output: True
#
# True when no 'x' and 'o' is present
# input: "zpzpzpp"
# output: True

# ======
# 1 variant
# ======

str = list(input("Input string "))

equiv = 0
let_1_0 = 'x'
let_1_1 = 'X'
let_2 = 'o'

for i in str:

    if i == let_1_1:
        i = let_1_0

    if i == let_1_0:
        equiv += 1
    elif i == let_2:
        equiv -= 1

if equiv == 0:
    # print(f'Amount "{let_1_0}" is equal amount "{let_2}"')
    output = True
elif equiv > 0:
    # print(f'Amount "{let_1_0}" is more than amount "{let_2}"')
    output = False
else:
    # print(f'Amount "{let_2}" is more than amount "{let_1_0}"')
    output = False

print(output)

# ======

# ======
# 2 variant
# ======

str = list(input("Input string "))

equiv_1 = 0
equiv_2 = 0
let_1 = 'xX'
let_2 = 'o'

for i in str:

    for let in let_1:
        if i == let:
            equiv_1 += 1

    if i == let_2:
        equiv_2 += 1

if equiv_1 == equiv_2:
    output = True
else:
    output = False

print(output)

# ======
# 3 variant
# ======

str = list(input("Input string "))

output = False
equiv_1, equiv_2 = [], []
let_1 = 'xX'
let_2 = 'o'

for i in str:

    for let in let_1:
        if i == let:
            equiv_1.append(i)

    if i == let_2:
        equiv_2.append(i)

if len(equiv_1) == len(equiv_2):
    output = True

print(output)