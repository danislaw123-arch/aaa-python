def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    v_lubom = moscow & kazan
    only_moscow = moscow - kazan
    only_kazan = kazan - moscow
    raznie = len(moscow | kazan)

    print(v_lubom)
    print(only_moscow)
    print(only_kazan)
    print(raznie)


if __name__ == '__main__':
    main()
