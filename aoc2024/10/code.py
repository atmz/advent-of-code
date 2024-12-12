import sys; sys.dont_write_bytecode = True; from util import *


def trails_from(x, y, grid):
    value = grid[y][x]
    # score = set()
    score=0
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        dx, dy = dir
        if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
            if grid[y+dy][x+dx] == value+1:
                if grid[y+dy][x+dx] == 9:
                    score+=1
                    # score.add((x+dx, y+dy))
                else:
                    score+=trails_from(x+dx, y+dy, grid)
                    # score=score.union(trails_from(x+dx, y+dy, grid))
    return score


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid = []
    antennas = defaultdict(list)
    for line in lines:
        grid.append([int(c) for c in line])
    score=0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c== 0:
                # score+=len(trails_from(x, y, grid))
                score+=trails_from(x, y, grid)
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
0123
1234
8765
9876""",
    r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)

