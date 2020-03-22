# method 1

ls = [2, 2, 2, 2, 2, 3, 3, 3, 3]
for i in ls:
    temp = []
    for j in ls:
        if i == j:
            temp.append(i)
        if len(temp) > 1 and len(temp) % 2:
            print(temp[0])
            break
    break

# method 2

ls = [2, 2, 2, 2, 2, 3, 3, 3, 3]
temp_ls = []
for i in ls:
    temp = []
    for j in ls:
        if i == j:
            temp.append(j)
    if temp in temp_ls:
        continue
    else:
        temp_ls.append(temp)

for i in temp_ls:
    if len(i) % 2:
        print(i[0])
