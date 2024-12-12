
import sys; sys.dont_write_bytecode = True; from util import *


def should_count_boundary(x,y,dir,set_counted_boundaries):
    # so if we have a horzontal line (i.e. dir is in the y axis)
    # we need to look and see if we've counted a boundary to the left or right
    # in the *same* direction (inside and outside sides are distinct)
    if dir[0] == 0:
        if (x-1, y, dir) in set_counted_boundaries or (x+1, y, dir) in set_counted_boundaries:
            return False
    else:
        if (x, y-1, dir) in set_counted_boundaries or (x, y+1, dir) in set_counted_boundaries:
            return False
    return True

def calculate_distinct_boundaries(set_boundaries):
    counted_boundaries = set()
    score=0
    boundaries_in_order = sorted(list(set_boundaries))
    for boundary in boundaries_in_order:
        if should_count_boundary(boundary[0], boundary[1], boundary[2], counted_boundaries):
            score+=1
        counted_boundaries.add(boundary)
    return score


def reigion_from_2(x, y, grid, region=None, set_counted_boundaries=None):
    value = grid[y][x]
    # score = set()
    if region is None:
        # Tuple of set of points, perimiter length
        region=(set(), 0)
    if set_counted_boundaries is None:
        set_counted_boundaries = set()
    region[0].add((x,y))

    for dir in [(1, 0),(0, 1), (-1, 0), (0, -1)]:
        dx, dy = dir
        if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
            candidate_point = (x+dx, y+dy)
            if candidate_point not in region[0]:
                if grid[y+dy][x+dx] == value:
                    a,b = reigion_from_2(x+dx, y+dy, grid, region, set_counted_boundaries)
                    # print(x,y,a,b, grid[y+dy][x+dx], "recursive call")
                    region= (region[0].union(a), b)
                else:
                    if should_count_boundary(x,y,dir,set_counted_boundaries):
                        # print("counted boundary", x,y, dir)
                        region = (region[0], region[1]+1)
                    set_counted_boundaries.add((x,y,dir))
                    
        else:
            if should_count_boundary(x,y,dir,set_counted_boundaries):
                region = (region[0], region[1]+1)
                # print("counted boundary", x,y, dir)
            set_counted_boundaries.add((x,y,dir))
    # print(set_counted_boundaries,region)
    region = (region[0], calculate_distinct_boundaries(set_counted_boundaries))
    return region


def reigion_from(x, y, grid, region=None):
    value = grid[y][x]
    # score = set()
    if region is None:
        # Tuple of set of points, perimiter length, incoming directions
        region=(set(), 0)
    region[0].add((x,y))
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        dx, dy = dir
        if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
            candidate_point = (x+dx, y+dy)
            if candidate_point not in region[0]:
                if grid[y+dy][x+dx] == value:
                    a,b = reigion_from(x+dx, y+dy, grid, region)
                    # print(x,y,a,b, grid[y+dy][x+dx], "recursive call")
                    region= (region[0].union(a), b)
                else:
                    # print(x,y, grid[y+dy][x+dx], "add boundary")
                    region = (region[0], region[1]+1)
        else:
            region = (region[0], region[1]+1)
            # print(x,y, y+dy,x+dx, "add boundary (off grid)")
    # print(x,y)
    return region


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid = []
    for line in lines:
        grid.append([c for c in line])
    regions = []
    all_visited = set()
    # new_region = reigion_from_2(0, 0, grid)
    # regions.append(new_region)

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if (x, y) not in all_visited:
                new_region = reigion_from_2(x, y, grid)
                regions.append(new_region)
                all_visited = all_visited.union(new_region[0])
    score=0
    for region in regions:
        print(len(region[0]), region[1], len(region[0]) * region[1])
        score += len(region[0]) * region[1]
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""",
    r"""AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA


""",r"""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE

""",r"""AAAA
BBCD
BBCC
EEEC


""",r"""
OOOOO
OXOXO
OOOOO
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

