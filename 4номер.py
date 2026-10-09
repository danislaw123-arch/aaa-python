days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

sum_vuruchka = 0
max_vuruchka = None
sredny_vuruchka = {}
vosvrat_20 = []

mmax = 0
for r in days:
    sum_vuruchka += r["revenue"]
    if r["revenue"] > mmax:
        max_vuruchka = r["day"]
        mmax = r["revenue"]
    sredny_vuruchka[r["day"]] = r["revenue"]/r["orders"]
    if r["returns"] / r["orders"] > 0.2:
        vosvrat_20.append(r["day"])

print(sum_vuruchka)
print(max_vuruchka)
print(sredny_vuruchka)
print(vosvrat_20)
