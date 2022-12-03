from typing import Union


class Rock:
    points = 1

    def __init__(self) -> None:
        pass

    def __str__(self):
        return "Rock"

    def win(self):
        return Scissors

    def lose(self):
        return Paper


class Paper:
    points = 2

    def __init__(self) -> None:
        pass

    def __str__(self):
        return "Paper"

    def win(self):
        return Rock

    def lose(self):
        return Scissors


class Scissors:
    points = 3

    def __init__(self) -> None:
        pass

    def __str__(self):
        return "Scissors"

    def win(self):
        return Paper

    def lose(self):
        return Rock


class Matches:
    ROCK = Rock
    PAPER = Paper
    SCISSORS = Scissors


def rsp_solve(p1: Union[Rock, Paper, Scissors], p2: Union[Rock, Paper, Scissors]):
    match type(p1):
        case Matches.ROCK:
            if isinstance(p2, Rock):
                return "Draw"
            if isinstance(p2, Paper):
                return p2
            if isinstance(p2, Scissors):
                return p1

        case Matches.PAPER:
            if isinstance(p2, Rock):
                return p1
            if isinstance(p2, Paper):
                return "Draw"
            if isinstance(p2, Scissors):
                return p2

        case Matches.SCISSORS:
            if isinstance(p2, Rock):
                return p2
            if isinstance(p2, Paper):
                return p1
            if isinstance(p2, Scissors):
                return "Draw"


op_mapper = {"A": Rock, "B": Paper, "C": Scissors}
mapper = {"X": "Lose", "Y": "Draw", "Z": "Win"}


if __name__ == "__main__":
    total = 0
    with open("data.txt", "r") as f:
        for line in f.readlines():
            _op = line.split(" ")[0]
            _mv = line.split(" ")[-1][0]
            op = op_mapper.get(_op)()
            mv = mapper.get(_mv)
            if mv == "Win":
                mv = op.lose()()
            if mv == "Lose":
                mv = op.win()()
            if mv == "Draw":
                mv = op_mapper.get(_op)()

            res = rsp_solve(op, mv)
            total += mv.points
            if res == "Draw":
                total += 3
            if isinstance(res, type(mv)):
                total += 6

    print(total)
