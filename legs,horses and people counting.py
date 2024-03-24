for lidi in range(0, 23):
    koni = 22 - lidi
    nohou = lidi * 2 + koni * 4
    if nohou == 72:
        print("lidi=" + str(lidi), end= "\t")
        print("koni=" + str(koni), end= "\t")
        print("nohou=" + str(nohou), end= "\t")