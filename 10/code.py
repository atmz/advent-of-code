import sys; sys.dont_write_bytecode = True; from util import *


def possible_moves(c):
    if c == '|':
        return ( (1,0) , (-1,0) )
    if c == '-':
        return ( (0,1) , (0,-1) )
    if c == 'L':
        return ( (-1,0) , (0, 1) )
    if c == 'J':
        return ( (-1,0) , (0,-1) )
    if c == '7':
        return ( (1,0) , (0,-1) )
    if c == 'F':
        return ( (1,0) , (0,1) )
    if c == 'S':
        return ( (1,0) , (0,1), (-1,0) , (0,-1) )
    else:
        return (  )

def search(start, goal, seen, map, distance):
    # print(f"search({start}, {goal}, {seen}, map, {distance})")
    # print(f"value:{map[start[0]][start[1]]}")
    # print(f"possible_moves:{possible_moves(map[start[0]][start[1]])}")
    max_y =  len(map)
    max_x =  len(map[0])
    seen.add(start)
    for (dy,dx) in possible_moves(map[start[0]][start[1]]):
        y = start[0]+dy
        x = start[1]+dx
        if (y,x) == goal and distance>2:
            print("found at",(distance+1)/2)
            return ((distance+1)/2, [start])
        if y>=0 and x>=0 and y< max_y and x<max_x and (y,x) not in seen:
            foo = search((y,x), goal, seen, map, distance+1)
            if foo:
                distance = foo[0]
                path = foo[1]
                path.append(start)
                return (distance, path)
    
def is_inside( point, path, lines):
    if point in path:
        return False
    crossings = 0
    last_was_crossing = False
    y = point[0]
    while y>0:
        y-=1
        if (y,point[1]) in path and lines[y][point[1]] in ['-','7','F']:
            print(f"point{point} - crossing{(y,point[1])}")
            if not last_was_crossing:
                crossings+=1
            last_was_crossing = True
        else:
            last_was_crossing = False
    if crossings % 2 == 1:
        print(f"inside - {crossings} - {point}")
        return True
    return False


def print_grid(grid):
    for row in grid:
        line = ''.join(str(f)[0] for f in row)
        print(line)

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    defaultdict_int = defaultdict(int)
    score = 0
    max_y =  len(lines)
    max_x =  len(lines[0])

    distances = make_grid(max_y, max_x, fill=99999999)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S' :
                start = (y,x)
    seen = set()
    distance, path = search(start, start, seen, lines, 0)
    print(f"Part 1: {int(distance)}")
    score = 0
    path = set(path)
    print(path)
    for y in range(0, max_y):
        for x in range(0, max_x):
            if is_inside((y,x), path, lines):
                score+=1
    print(f"Part 2: {int(score)}")
    
    for y in range(0, max_y):
        lines[y] = list(lines[y])
        for x in range(0, max_x):
            if not (y,x) in path:
                lines[y][x]='.'
            else:
                lines[y][x]=' '
    print_grid(lines)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""",
    r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........


""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)

