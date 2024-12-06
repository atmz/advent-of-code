import sys; sys.dont_write_bytecode = True; from util import *


def possible_moves(y,x , grid, i):
    result = []
    for move in [ (1,0) , (0,1), (-1,0) , (0,-1) ]:
        candidate = (y+move[0], x+move[1], i)
        if grid[
                candidate[0] % len(grid)
            ][
                candidate[1] % len(grid[0])
            ] == '.':
            result.append(candidate)
    return result


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    grid = [list(row) for row in inp.splitlines()]

    max_y =  len(grid)
    max_x =  len(grid[0])
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == 'S' :
                start = (y,x)
                grid[y][x] = '.'

    current = { (start[0], start[1], 0) }
    next = set()
    previous_count = 1
    previous_diff = 0
    for step in range(0,5000):
        for source in current:
            for move in possible_moves(source[0], source[1] , grid, step):
                if move not in next:
                    next.add(move)
        current = next
        next = set()
        previous_diff_diff = (len(current)-previous_count)-previous_diff
        previous_diff = len(current)-previous_count
        print(f"{step+1} steps - {len(current)} - diff - {previous_diff} - diff2 - {previous_diff_diff}")
            

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
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

