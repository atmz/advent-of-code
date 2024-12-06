import sys; sys.dont_write_bytecode = True; from util import *



def roll_north(grid):
    for x in range(0,len(grid[0])):
        sorted_col = "#".join(["".join(sorted(list(z), reverse=True)) for z in ("".join([grid[y][x] for y in range(0,len(grid))]).split('#'))])
        for y,c in enumerate(sorted_col):
            grid[y][x] = c

def roll_south(grid):
    for x in range(0,len(grid[0])):
        sorted_col = "#".join(["".join(sorted(list(z))) for z in ("".join([grid[y][x] for y in range(0,len(grid))]).split('#'))])
        for y,c in enumerate(sorted_col):
            grid[y][x] = c


def roll_east(grid):
    for y in range(0,len(grid)):
        sorted_rows = "#".join(["".join(sorted(list(z))) for z in ("".join([grid[y][x] for x in range(0,len(grid[0]))]).split('#'))])
        for x,c in enumerate(sorted_rows):
            grid[y][x] = c


def roll_west(grid):
    for y in range(0,len(grid)):
        sorted_rows = "#".join(["".join(sorted(list(z), reverse=True)) for z in ("".join([grid[y][x] for x in range(0,len(grid[0]))]).split('#'))])
        for x,c in enumerate(sorted_rows):
            grid[y][x] = c




def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid = [list(x) for x in lines]

    last = 0
    for i in range(0,300):
        score = 0
        # print(f"Cycle {i+1}")
        roll_north(grid)
        roll_west(grid)
        roll_south(grid)
        roll_east(grid)

        # print_grid(grid)

        for x in range(0,len(grid[0])):
            sorted_col = "".join([grid[y][x] for y in range(0,len(grid))])
            for j,c in enumerate(sorted_col):
                if c=='O':
                    score+=len(sorted_col)-j
        print(score,  (i+1) % 7)
        last=score
    print(1000000000 % 7)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""",
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

