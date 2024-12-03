def readData() -> str:
    with open("./data.txt", "r") as f:
        data = f.read()
    return data


def isMul(s: str) -> bool:
    return s[:3] == "mul"


def isDo(s: str) -> bool:
    return s[:4] == "do()"


def isDont(s: str) -> bool:
    return s[:7] == "don't()"


def switchDo(s: str) -> bool | None:
    if isDo(s):
        return True
    if isDont(s):
        return False
    return None


def parseMul(st: str) -> int | None:
    if st[3] != "(":
        return
    stopChr = st.find(")")
    if not stopChr:
        return

    split = st[3 : stopChr + 1]
    raw = "".join([i for i in split if i not in ("(", ")")]).split(",")
    if len(raw) != 2 or not raw[0].isnumeric() or not raw[-1].isnumeric():
        return
    return int(raw[0]) * int(raw[-1])


def solution():
    res = 0
    isEnabled = True
    data = readData()
    for i in range(len(data) - 2):
        switch = switchDo(data[i:])
        if switch is not None:
            isEnabled = switch
        if isEnabled:
            if isMul(data[i : i + 3]):
                if ret := parseMul(data[i:]):
                    res += ret
    return res


print(solution())
