import os, sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"> Usage: python3 {sys.argv[0]} [filename]")
        sys.exit(1)

    t = f"""class Solution:
    def __init__(self, filename: str = "./{sys.argv[1]}/input.txt"):
        with open(filename, "r") as f:
            self.input = ...

    def solve(self):
        ...

if __name__ == '__main__':
    print(Solution().solve())"""

    os.mkdir(sys.argv[1])
    with open(f"./{sys.argv[1]}/p1.py", "w") as f:
        f.write(t)
    with open(f"./{sys.argv[1]}/p2.py", "w") as f:
        f.write(t)
    