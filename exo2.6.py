n = int(input("Taille du tableau ? : "))
tab = []

for i in range(n):
    num = int(input())
    tab.append(num)

somme = 0

for j in tab:
    somme += j

moyenne = somme / n

res = []

for k in tab:
    if k > moyenne:
        res.append(k)

print(res)