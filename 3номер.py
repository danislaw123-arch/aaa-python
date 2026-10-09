orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

vosvrat = 0
vernul = set()
dostavleno = 0
summ_check = 0

for r in orders:
    if r["status"] == "returned":
        vosvrat += r["amount"]
        vernul.add(r["buyer"])
    elif r["status"] == "delivered":
        dostavleno += 1
        summ_check += r["amount"]

sred_check = summ_check/dostavleno

print(vosvrat)
print(vernul)
print(dostavleno)
print(sred_check)
