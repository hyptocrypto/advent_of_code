def readData() -> list[list]:
    with open("./data.txt", "r") as f:
        data = f.read()
    ret = []
    for i in data.split("\n"):
        ret.append([int(d) for d in i.split(" ") if d.isnumeric()])
    return [i for i in ret if i != []]


def inc_or_dec(i: list) -> tuple[bool, bool]:
    inc, dec = False, False
    if i[0] > i[1]:
        dec = True
    if i[0] < i[1]:
        inc = True
    return inc, dec


def is_safe_list(i):
    inc, dec = inc_or_dec(i)
    if not any((inc, dec)):
        return False

    if inc:  # Check incrementing condition
        for j in range(len(i) - 1):
            if i[j] >= i[j + 1]:  # Not strictly increasing
                return False
            diff = i[j + 1] - i[j]
            if not (1 <= diff <= 3):  # Difference not in range
                return False

    if dec:  # Check decrementing condition
        for j in range(len(i) - 1):
            if i[j] <= i[j + 1]:  # Not strictly decreasing
                return False
            diff = i[j] - i[j + 1]
            if not (1 <= diff <= 3):  # Difference not in range
                return False

    return True


def solution():
    safe = 0
    data = readData()
    for i in data:
        if is_safe_list(i):
            safe += 1
            continue

        for j in range(len(i)):
            modified_list = i[:j] + i[j + 1 :]  # Remove one element
            if is_safe_list(modified_list):
                safe += 1
                break
    return safe


print(solution())
