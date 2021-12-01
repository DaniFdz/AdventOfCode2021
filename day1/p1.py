class Solution:
    def __init__(self, filename: str = "./day1/input.txt"):
        with open(filename, "r") as f:
            self.input = [int(x) for x in f.read().split("\n")[:-1]]

    def solve(self):
        total = 0
        for i, x in enumerate(self.input[1:]):
            if x > self.input[i]:
                total += 1
        return total

if __name__ == '__main__':
    print(Solution().solve())