from dataclasses import dataclass

@dataclass
class Move:
    d: str
    v: int

class Solution:
    def __init__(self, filename: str = "./day2/input.txt"):
        with open(filename, "r") as f:
            self.input = []
            for y in f.read().split("\n")[:-1]:
                x = y.split(" ")
                self.input.append(Move(x[0][0], int(x[1])))

    def solve(self):
        depth, pos = 0, 0
        for move in self.input:
            if move.d == "f":
                pos += move.v
            elif move.d == "d":
                depth += move.v
            else:
                depth -= move.v
        return depth * pos

if __name__ == '__main__':
    print(Solution().solve())