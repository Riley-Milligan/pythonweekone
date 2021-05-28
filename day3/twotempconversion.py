def tempFtoC(x):
    return round(((x - 32) / 9) * 5)


def tempCtoF(x):
    return round(((x / 5) * 9) + 32)


print(tempFtoC(45))

print(tempCtoF(60))
