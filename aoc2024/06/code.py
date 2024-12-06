import sys; sys.dont_write_bytecode = True; from util import *


            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    def turn_right(d):
        if d == (0, -1):
            return (1, 0)
        if d == (1, 0):
            return (0, 1)
        if d == (0, 1):
            return (-1, 0)
        if d == (-1, 0):
            return (0, -1)
    d_to_char = {
        (0, -1): '^',
        (0, 1): 'v',
        (-1, 0): '<',
        (1, 0): '>'
    }
    char_to_d = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    lines = inp.splitlines()
    grid = []
    d = None
    current =  None
    for line in lines:
        grid.append([c for c in line])
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c in char_to_d.keys():
                d = char_to_d[c]
                current = (x, y)   
                initial_d = char_to_d[c]
                initial_current = (x, y)
    try:
        while current[1]>=0 and current[0]>=0:# negative won't trigger IndexError, so we still need bounds check
            grid[current[1]][current[0]] = 'X'
            new_current = (current[0]+d[0], current[1]+d[1])
            while grid[new_current[1]][new_current[0]] == '#':
                d = turn_right(d)
                new_current = (current[0]+d[0], current[1]+d[1])
            current = new_current
            
    except IndexError:
        pass


    for line in grid:
        print ("".join(line))
    print (sum([line.count("X") for line in grid]))

    # part 2
    score = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            seen = set()
            d = initial_d
            current = initial_current
            obstacle = (x,y)
            if grid[y][x] != 'X' or (x,y) ==initial_current: # obstacles placed not in the path wont do anything, and we can't put one in the starting spot
                continue
            try:
                while current[1]>=0 and current[0]>=0: # negative won't trigger IndexError, so we still need bounds check
                    new_current = (current[0]+d[0], current[1]+d[1])
                    while grid[new_current[1]][new_current[0]] == '#' or new_current == obstacle:
                        d = turn_right(d)
                        new_current = (current[0]+d[0], current[1]+d[1])
                    current = new_current
                    if (current[0], current[1], d) in seen:
                        score+=1
                        break
                    seen.add((current[0], current[1], d))
                    
            except IndexError:
                pass

    
    print (score)

    def to_color(c, i):
        import colorsys
        if c=="#":
            return (255,255,255)
        elif c in char_to_d.keys():
            return (0,255,0)
        elif c == "X":
            return (64,64,64)
        elif c == "Y":
            i = i % 255
            r,g,b = colorsys.hls_to_rgb(float(i)/255, .8,1)
            return (int(255*r),int(255*g),int(255*b))

        
        return (0,0,0)

    def save_grid(grid,i):
        with open(f"out{i}.ppm", "w") as f:
            f.write("P3\n")
            f.write(f"{len(grid[0])} {len(grid)}\n")
            f.write("255\n")
            for row in grid:
                for c in row:
                    f.write(f"{c[0]} {c[1]} {c[2]} ")
    # animations
    lines = inp.splitlines()
    ppm_grid = []
    for line in lines:
        ppm_grid.append([to_color(c,0) for c in line])
    save_grid(ppm_grid, 0)
    file_i=0
    color_i = 0
    score = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            color_i+=3
            seen = set()
            d = initial_d
            current = initial_current
            obstacle = (x,y)
            if grid[y][x] != 'X' or (x,y) ==initial_current: # obstacles placed not in the path wont do anything, and we can't put one in the starting spot
                continue
            new_grid = deepcopy(grid)
            try:
                while current[1]>=0 and current[0]>=0: # negative won't trigger IndexError, so we still need bounds check
                    new_current = (current[0]+d[0], current[1]+d[1])
                    while grid[new_current[1]][new_current[0]] == '#' or new_current == obstacle:
                        d = turn_right(d)
                        new_current = (current[0]+d[0], current[1]+d[1])
                    current = new_current
                    if (current[0], current[1], d) in seen:
                        score+=1
                        break
                    seen.add((current[0], current[1], d))
                    if (current[0],current[1]) != initial_current:  
                        ppm_grid[current[1]][current[0]] = to_color("Y", color_i)
                        new_grid[current[1]][current[0]] = "X"
                    file_i+=1
                    save_grid(ppm_grid, file_i)
                    
            except IndexError:
                pass
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
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

