if __name__ == "__main__":
    overlap = 0
    data = open("data.txt", "r").read().strip()
    pairs = data.split("\n")
    for pair in pairs:
        (a1, a2, b1, b2,) = [
            int(item) for sub in [i.split("-") for i in pair.split(",")] for item in sub
        ]

        if (a1 >= b1 and a1 <= b2) or (b1 >= a1 and b1 <= a2):
            overlap += 1
            print(pair)
            print("a1", "a2", "b1", "b2")
    print(overlap)
