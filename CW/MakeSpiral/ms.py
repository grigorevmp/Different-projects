def spiralize(size):
    # Make a snake

    # Your task, is to create a NxN spiral with a given size.
    #
    # For example, spiral with size 5 should look like this:
    #
    # 00000
    # ....0
    # 000.0
    # 0...0
    # 00000

    spiral = dict(zip(list(range(1, size + 1)), ([1] * size for _ in range(1, size + 1))))
    upShift = 2
    sideShift = 0

    while True:
        try:
            hup = spiral[upShift]
            for i in range(sideShift, size - 1):
                hup[i] = 0
                spiral[upShift] = hup

            for i in range(upShift, size):
                rvt = spiral[i]
                rvt[size - 2] = 0
                spiral[i] = rvt

            hbt = spiral[size - 1]
            for i in range(sideShift + 1, size - 1):
                hbt[i] = 0
                spiral[size - 1] = hbt

            for i in range(upShift + 2, size):
                vlt = spiral[i]
                vlt[sideShift + 1] = 0
                spiral[i] = vlt

            upShift += 2
            sideShift += 2
            size -= 2

        except Exception:
            return [spiral[x] for x in sorted(spiral.keys())]


print(spiralize(5))
