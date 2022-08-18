A = set(["a", "b", "c", "d"])
B = set(["b", "e", "d", "f"])
C = set(["x", "e", "c", "h"])

    # a
A.update(C)
    # b
B.intersection(C)
    # c
A.symmetric_difference(B)
    # d
A.add("m")
B.add("n")
C.add("o")

