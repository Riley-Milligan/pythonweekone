stars = ([], [], [], [], [], [], [], [], [])

for i in range(0, 5):
    for x in range(i, 5):
        stars[x].append("*")

y = 0

for i in range(8, 4, -1):
    y += 1
    for x in range(0, y):
        stars[i].append("*")

for i in stars:
    print(*i)
