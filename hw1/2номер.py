def main():
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
    ]

    print(len(queries))

    skolko = {}
    for r in queries:
        if r in skolko:
            skolko[r] += 1
        else:
            skolko[r] = 1
    print(skolko)

    mmax = 0
    pops = None
    for r in queries:
        if skolko[r] > mmax:
            pops = r
            mmax = skolko[r]
    print(pops)

    print(skolko[pops] / len(queries))

    once = []
    for r in queries:
        if skolko[r] == 1:
            once.append(r)

    print(once)


if __name__ == '__main__':
    main()