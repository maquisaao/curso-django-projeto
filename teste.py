def transform(a=2):
    if a == 1:
        return a+2
    return a


total = 1

for x in [3, 5, 1]:
    total = total+transform(x)

teste = transform(2)
print(teste)
