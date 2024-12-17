
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


def count_space_in_direction(grid, x, y, dir):
    # Calculate total empty space before we hit a wall
    # Ignore boxes, but don't break. 
    # After, we'll squish all the boxes into the wall
    space=0
    dx, dy = dir
    while(grid[y+dy][x+dx] != '#'):
        if grid[y+dy][x+dx] == '.':
            space+=1
        dx+=dir[0]
        dy+=dir[1]
    # print("space",space)
    return space

def score(grid):
    score=0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
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
        grid.append([c for c in line])
        i+=1
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
        spaces_to_move = count_space_in_direction(grid, robot[0], robot[1], inst_to_dir(instr))
        if spaces_to_move > 0:
            dx, dy =  inst_to_dir(instr)
            x,y = robot
            grid[y][x] = '.'
            x+=dx
            y+=dy
            old_value = grid[y][x]
            grid[y][x] = '@'
            robot = (x,y)
            if old_value == 'O':
                while grid[y][x] != ".":
                    x+=dx
                    y+=dy       
                grid[y][x] = 'O'
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

