tab1 = [9, 12, 3, 7]
tab2 = [2, 1, 12, 8]
n = 0
for i in range(len(tab1)):
    for j in range(len(tab2)):
        n = n + tab1[i] * tab2[j]

print(n)