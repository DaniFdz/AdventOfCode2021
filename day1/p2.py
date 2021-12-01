class Solution:
    def __init__(self, filename: str = "./day1/input.txt"):
        with open(filename, "r") as f:
            inp = {}
            for i, x in enumerate(f.read().split("\n")[:-1]):
                for j in range(i-2, i+1):
                    if j >= 0:
                        if j in inp:
                            inp[j].append(int(x))
                        else:
                            inp[j] = [int(x)]       
            self.input = {key: sum(value) for key, value in inp.items()}         

    def solve(self):
        l = list(self.input.values())
        total = 0
        for i, x in enumerate(l[1:]):
            if x > l[i]:
                total += 1
        return total

if __name__ == '__main__':
    print(Solution().solve())