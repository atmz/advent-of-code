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
    

def calculate_s(point, path):
    for c in list("I-LJ7F"):
        all_in_path = True
        for (dy,dx) in possible_moves(point):
            y = point[0]+dy
            x = point[1]+dx
            if (y,x) not in path:
                all_in_path = False
            if all_in_path:
                return c

def is_inside( point, path, lines):
    x = point[1]
    track_from_top = [lines[y][x] for y in range(0,point[0])]
    outside = True
    vertical_pipe_start = ''
    for y,c in enumerate(track_from_top):
        if c == 'S':
            c = calculate_s( (y,x), path)
        if c == '-'  and (y,x) in path:
            outside = not outside
        if c in ['7', 'F'] and (y,x) in path:
            vertical_pipe_start = c
        if c == 'L' and (y,x) in path:
            if vertical_pipe_start == '7':
                outside = not outside
            vertical_pipe_start = ''
        if c == 'J' and (y,x) in path:
            if vertical_pipe_start == 'F':
                outside = not outside
            vertical_pipe_start = ''
    return not outside


def print_grid(grid):
    for row in grid:
        line = ''.join(str(f)[0] for f in row)
        print(line)

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

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


    path = set(path)
    inside = set()
    print(path)
    printable_grid = copy.deepcopy(lines)
    for y in range(0, max_y):
        printable_grid[y]  = list(printable_grid[y])
        lines[y] = list(lines[y])
        for x in range(0, max_x):
            if (y,x) in path:
                printable_grid[y][x]='*'
            elif is_inside((y,x), path, lines):
                inside.add((y,x))
                printable_grid[y][x] = 'I'
            else:
                printable_grid[y][x] = 'O' 
                
    print_grid(printable_grid)
    print(inside)

    print(f"Part 2: {len(inside)}")
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
r"""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L



""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)

