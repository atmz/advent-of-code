import sys; sys.dont_write_bytecode = True; from util import *


def get_inside_points( x,y, global_inside, global_outside):
    next = set()
    seen = set()
    next.add( (x, y) )
    while next:
        new_next = set()
        for point in next:
            x, y = point
            if (x,y) in global_outside:
                return set(), seen
            for new_x in range(x-1,x+2):
                for new_y in range(y-1,y+2):
                    if (new_x, new_y) not in global_inside and (new_x, new_y) not in seen:
                        new_next.add((new_x, new_y))
                        seen.add((new_x, new_y)) 
        next = new_next
    
    return seen, set()



def print_grid(grid):
    for row in grid:
        line = ''.join(str(f)[0] for f in row)
        print(line)


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    score=0
    x = 0
    y = 0
    max_x = -99999
    max_y = -99999
    min_x = 99999
    min_y = 99999
    grid = defaultdict(lambda: defaultdict(str))
    distances = []
    for line in lines:
        if len(line)>3:
            # Part 1
            # direction, distance, color =  line.split()
            # Part 2
            _, _, hex =  line.split()
            direction = hex[-2]
            distance = int(hex[2:-2], 16)
            distances.append(distance)
            for i in range(0,int(distance)):
                grid[x][y]='#'
                if direction == 'U' or direction=='3':
                    y-=1
                if direction == 'D' or direction=='1':
                    y+=1
                if direction == 'R' or direction=='0':
                    x+=1
                if direction == 'L' or direction=='2':
                    x-=1
        max_x = max(x,max_x)
        max_y = max(y,max_y)
        min_x = min(x,min_x)
        min_y = min(y,min_y)
    score=0
    outside = set()
    inside = set()
    for x in grid:
        for y in grid[x]:
            inside.add((x,y))
    outside.add( (min_x, min_y-1))
    outside.add( (max_x, min_y-1))
    outside.add((min_x, max_y+1))
    outside.add((max_x, max_y-1) )
    for y in range(min_y,max_y):
        for x in range(min_x,max_x):
             if (x,y) not in inside and (x,y) not in outside:
                new_inside, new_outside = get_inside_points(x,y,inside, outside) 
                inside.update(new_inside)
                outside.update(new_outside)
        

    print(f"score: {len(inside)}")

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
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

