def readData() -> tuple[list, list]:
    with open("./data.txt", "r") as f:
        data = f.read()
    l1 = []
    l2 = []
    for i in [d.split(" ") for d in data.split("\n")]:
        if len(i) == 4:
            l1.append(int(i[0]))
            l2.append(int(i[-1]))
    return sorted(l1), sorted(l2)


def solution():
    l1, l2 = readData()
    return sum(i * l2.count(i) for i in l1)


print(solution())
