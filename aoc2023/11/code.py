import sys; sys.dont_write_bytecode = True; from util import *


def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def distance2(a,b, cols, rows):
    col_extra = 0
    row_extra = 0
    for i in range(*sorted([a[0],b[0]])):
        if i in rows:
            row_extra+=999999
    for i in range(*sorted([a[1],b[1]])):
        if i in cols:
            col_extra+=999999

    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + row_extra + col_extra

def expand(grid):
    i = 0
    galaxies = []
    colcounts=set([i for i in range(0,len(grid[0]))])
    while i<len(grid):
        rowcount=0
        for j, c in enumerate(grid[i]):
            if c=="#":
                print(j)
                if j in colcounts:
                    colcounts.remove(j)
                rowcount+=1
        if rowcount == 0:
            grid.insert(i,copy.deepcopy(grid[i]))
            i+=1
        i+=1
    for row in grid:
        for key in sorted(list(colcounts), reverse=True):
            row.insert(key,'.')

def get_empty_cols_and_rows(grid):    
    cols=set([i for i in range(0,len(grid[0]))])
    rows=set()
    for i, row in enumerate(grid):
        rowcount=0
        for j, c in enumerate(row):
            if c=="#":
                if j in cols:
                    cols.remove(j)
                rowcount+=1
        if rowcount == 0:
            rows.add(i)
    return cols, rows



def print_grid(grid):
    for row in grid:
        line = ''.join(str(f)[0] for f in row)
        print(line)

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    grid = [list(x) for x in inp.splitlines()]

    print_grid(grid)
    # expand(grid)
    print_grid(grid)

    galaxies = []
    
    for y, row in enumerate(grid): 
        for x, c in enumerate(row):
            if c=="#":
                galaxies.append( (y,x) )
    
    distances = {}
    score = 0
    pairs=0
    while galaxies:
        g1 = galaxies.pop()
        for g2 in galaxies:
            key = sorted([g1,g2])
            d = distance(g1,g2)
            score+=d
            pairs+=1

    print(pairs)
    print(score)

    # Part 2

    for y, row in enumerate(grid): 
        for x, c in enumerate(row):
            if c=="#":
                galaxies.append( (y,x) )

    cols, rows  = get_empty_cols_and_rows(grid)
    print(cols, rows)
    score = 0
    pairs=0
    while galaxies:
        g1 = galaxies.pop()
        for g2 in galaxies:
            key = sorted([g1,g2])
            d = distance2(g1,g2, cols, rows)
            score+=d
            pairs+=1

    print(pairs)
    print(score)



    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
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

