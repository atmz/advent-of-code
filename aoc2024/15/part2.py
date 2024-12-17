
import sys; sys.dont_write_bytecode = True; from util import *

def inst_to_dir(inst):
    if inst == '^':
        return (0, -1)
    if inst == 'v':
        return (0, 1)
    if inst == '<':
        return (-1, 0)
    if inst == '>':
        return (1, 0)
    assert False


def move_in_direction(grid, x, y, dir):
    print(x,y)
    dx, dy = dir
    boxes_to_move = []
    if dy == 0:
        while True:
            if grid[y][x+dx] == '[':
                boxes_to_move.append((x+dx, y+dy, '['))
            elif grid[y][x+dx] == ']':
                boxes_to_move.append((x+dx, y+dy, ']'))
            elif grid[y][x+dx] == '.':
                break
            elif grid[y][x+dx] == '#':
                return False
            dx+=dir[0]
    else:
        x_coords = {x}
        while True:
            new_x_coords=set()
            values = [grid[y+dy][ax] for ax in x_coords]
            if '#' in values:
                return False
            elif '[' in values or ']' in values:
                for ax in x_coords:
                    if grid[y+dy][ax] == '[':
                        boxes_to_move.append((ax, y+dy, '['))
                        boxes_to_move.append((ax+1, y+dy, ']'))
                        new_x_coords.add(ax)
                        new_x_coords.add(ax+1)
                    if grid[y+dy][ax] == ']':
                        boxes_to_move.append((ax, y+dy,']'))
                        boxes_to_move.append((ax-1, y+dy,'['))
                        new_x_coords.add(ax)
                        new_x_coords.add(ax-1)
            else: # no boxes or walls, we're good
                break
            x_coords = new_x_coords
            dy+=dir[1]
    dx, dy = dir
    if boxes_to_move:
        print(boxes_to_move, dir)
        for box in boxes_to_move:
            grid[box[1]][box[0]] = '.'
        for box in boxes_to_move:
            grid[box[1]+dy][box[0]+dx] = box[2]
    print(x,y)
    grid[y][x] = '.'
    grid[y+dy][x+dx] = '@'

def score(grid):
    score=0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "[":
               score+=100*y+x
    return(score)

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid = []
    instructions = []
    robot = None
    i=0
    while True:
        line = lines[i]
        if len(line) == 0:
            break
        gridline=""
        for c in line:
            if c == "@":
                gridline+="@."
            if c == "O":
                gridline+="[]"
            if c == ".":
                gridline+=".."
            if c == "#":
                gridline+="##"
        
        grid.append([c for c in gridline])
        i+=1
    for line in grid:
        print("".join(line))
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
               robot = (x, y) 
    for line in lines[i:]:
        for inst in line:
            if inst in ['<' , '>', '^', 'v']:
                instructions.append(inst)
    
    for line in grid:
        print("".join(line))

    for instr in instructions:
        move_in_direction(grid, robot[0], robot[1], inst_to_dir(instr))
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "@":
                    robot = (x, y) 
        print("\n") 
        print(instr) 
        for line in grid:
            print("".join(line))
    print(score(grid))
    
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
,r"""

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

