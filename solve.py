from typing import List
from dataclasses import dataclass

class Rock:
    def __init__(self) -> None:
        pass
class Paper:
    def __init__(self) -> None:
        pass
class Scissors:
    def __init__(self) -> None:
        pass
        

def rsp_solve(p1, p2):
    match p1:
        case isinstance(p1, Rock):
            if isinstance(p2, Rock):
                return "Draw"
            isinstance(p2, Paper):
                return p2
            isinstance(p2, Scissors):
                
        case isinstance(p1, Paper):
            pass
        case isinstance(p1, Scissors):
            pass


if __name__ == '__main__':
    