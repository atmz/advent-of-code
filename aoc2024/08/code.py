import sys; sys.dont_write_bytecode = True; from util import *

            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid = []
    antipode_grid = []
    antennas = defaultdict(list)
    for line in lines:
        grid.append([c for c in line])
        antipode_grid.append(['.' for c in line])

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c!= '.':
                antennas[c].append((x, y))
         
    print(antennas)
    for line in grid:
        print ("".join(line))

    for a, locs in antennas.items():
        for combination in itertools.combinations(locs, 2):
            difference = (combination[1][0]-combination[0][0], combination[1][1]-combination[0][1])
            potential_points = [
                (combination[0][0]+difference[0], combination[0][1]+difference[1]),
                (combination[1][0]-difference[0], combination[1][1]-difference[1]),
                (combination[0][0]-difference[0], combination[0][1]-difference[1]),
                (combination[1][0]+difference[0], combination[1][1]+difference[1])
            ]
            for point in potential_points:
                if point!= combination[0] and point!= combination[1] and point[0]>=0 and point[1]>=0 and point[0]<len(grid[0]) and point[1]<len(grid):
                    antipode_grid[point[1]][point[0]] = a
    score = 0
    for line in antipode_grid:
        print ("".join(line))
        score += len(line)-line.count('.')
    print(score)

    # Part 2:
    antipode_grid=[]
    for line in lines:
        antipode_grid.append(['.' for c in line])

    for a, locs in antennas.items():
        for combination in itertools.combinations(locs, 2):
            difference = (combination[1][0]-combination[0][0], combination[1][1]-combination[0][1])
            gcd = math.gcd(difference[0], difference[1])
            difference = (difference[0]//gcd, difference[1]//gcd)
            potential_points = [
                (combination[0][0]+difference[0], combination[0][1]+difference[1]),
                (combination[1][0]+difference[0], combination[1][1]+difference[1]),
            ]
            for point in potential_points:
                while point[0]>=0 and point[1]>=0 and point[0]<len(grid[0]) and point[1]<len(grid):
                    antipode_grid[point[1]][point[0]] = a
                    point = (point[0]+difference[0], point[1]+difference[1])
            potential_points = [
                (combination[1][0]-difference[0], combination[1][1]-difference[1]),
                (combination[0][0]-difference[0], combination[0][1]-difference[1]),
            ]
            for point in potential_points:
                while point[0]>=0 and point[1]>=0 and point[0]<len(grid[0]) and point[1]<len(grid):
                    antipode_grid[point[1]][point[0]] = a
                    point = (point[0]-difference[0], point[1]-difference[1])
    score = 0
    print("antipoles")
    for line in antipode_grid:
        print ("".join(line))
        score += len(line)-line.count('.')
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""",
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

