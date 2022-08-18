for i in range(2, 100):

    a = False
    for n in range(2, i):

        if i % n == 0:
            a = True
            break
        else:
            a = False

    if a == False:
        print(i)
