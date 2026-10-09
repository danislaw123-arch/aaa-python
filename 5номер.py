reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

sums = {}
chislo_otsuvuv = {}
chislo_1_2 = 0

for r in reviews:
    name = r["product"].lower()

    if name in sums:
        sums[name] += r["stars"]
        chislo_otsuvuv[name] += 1
    else:
        sums[name] = r["stars"]
        chislo_otsuvuv[name] = 1

    if r["stars"] <= 2:
        chislo_1_2 += 1

sredniy = {}
for r in sums:
    sredniy[r] = sums[r]/chislo_otsuvuv[r]
print(sredniy)

worst = None
worst_snach = None
for r in sredniy:
    if chislo_otsuvuv[r] >= 2:
        if worst_snach is None or sredniy[r] < worst_snach:
            worst = r
            worst_snach = sredniy[r]
print(worst)

print(chislo_1_2)

print(chislo_1_2 / len(reviews))
