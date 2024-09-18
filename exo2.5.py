tab = [99,55,100,62]

num = 0

for y,i in enumerate(tab):
    if num < i:
        num = i
        position = y + 1
        
print(num,position)