#v1

num = [1, 2, 3, 3, 3, 3, 1, 1, 1]

for i in num:
    dublicat = []
    for j in num:
        if i == j:
            dublicat.append(i)
    if len(dublicat) % 2 and len(dublicat) >= 1:
        print(dublicat[0])
        break

#v3 пока не придумала :(