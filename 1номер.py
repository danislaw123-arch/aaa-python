moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

v_lubom = moscow & kazan
only_Moscow = moscow - kazan
only_Kazan = kazan - moscow
raznie = len(moscow | kazan)

print(v_lubom)
print(only_Moscow)
print(only_Kazan)
print(raznie)
