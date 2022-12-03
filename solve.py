from typing import List
from dataclasses import dataclass


@dataclass
class Elf:
    items: List[int]

    def total_cal(self):
        return sum(self.items)


if __name__ == '__main__':
    elves: List[Elf] = []
    totals: List[int] = []
    _res = []
    with open("data.txt", "r") as f:
        for line in f.readlines():
            if line[0].isnumeric():
                _res.append(int(line))
            else:
                elf = Elf(items=_res)
                totals.append(elf.total_cal())
                _res.clear()

    totals.sort(reverse=True)
    print(totals[:3])
    print(sum(totals[:3]))