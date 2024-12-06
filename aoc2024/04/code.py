import sys; sys.dont_write_bytecode = True; from util import *


            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    dlines = []
    vlines = []
    grid = []
    for line in lines:
        grid.append(line)
    
    for i in range(0,len(grid[0])):
        lines.append("".join([line[i] for line in grid if i<len(line)]))
        #daigonal
        diagonal = ""
        x = i
        y = 0
        while y<len(grid) and x<len(grid[y]) :
            diagonal+=grid[y][x]
            y+=1
            x+=1
        lines.append(diagonal)
    
        diagonal = ""
        x = i
        y = 0
        while y<len(grid) and x>=0 :
            diagonal+=grid[y][x]
            y+=1
            x-=1
        lines.append(diagonal)
    
    for i in range(1,len(grid)):
        diagonal = ""
        x = 0
        y = i
        while y<len(grid) and x<len(grid[y]) :
            diagonal+=grid[y][x]
            y+=1
            x+=1
        lines.append(diagonal)
        diagonal = ""
        x = len(grid[0])-1
        y = i
        while y<len(grid) and x>0:
            diagonal+=grid[y][x]
            y+=1
            x-=1
        lines.append(diagonal)
    score = 0
    for line in lines:
        matches = re.findall(r"XMAS", line)
        matches += re.findall(r"SAMX", line)
        score+= len(matches)
    print(score)
    

    # part 2
    # what we want here is an ''A' surrounded by 2 'M's and 2 'S's
    # either:
    #  M.S
    #  .A.
    #  M.S
    # or:
    #  .M.
    #  SAM
    #  .S.
    score=0
    # so, for each 'A', let's check if it satisfies the rules

    new_grid = []
    for line in grid:
        new_grid.append(["." for l in line])
    for y in range(0,len(grid)):
        grid[y] = [c for c in grid[y]]

    for x in range(1, len(grid[0])-1):
        for y in range(1, len(grid)-1):
            xmas = False
            if grid[y][x] == 'A':
                #diagonal case:
                if (grid[y-1][x-1] == 'M' and grid[y+1][x+1] == 'S') or (grid[y-1][x-1] == 'S' and grid[y+1][x+1] == 'M'):
                    if (grid[y+1][x-1] == 'M' and grid[y-1][x+1] == 'S') or (grid[y+1][x-1] == 'S' and grid[y-1][x+1] == 'M'):
                        xmas = True
                        new_grid[y-1][x-1]=grid[y-1][x-1]
                        new_grid[y+1][x-1]=grid[y+1][x-1]
                        new_grid[y-1][x+1]=grid[y-1][x+1]
                        new_grid[y+1][x+1]=grid[y+1][x+1]
                # # horizontal case
                # if grid[y-1][x] == 'M' and grid[y+1][x] == 'S' or grid[y-1][x] == 'S' and grid[y+1][x] == 'M':
                #     if grid[y][x-1] == 'M' and grid[y][x+1] == 'S' or grid[y][x-1] == 'S' and grid[y][x+1] == 'M':
                #         xmas = True
                #         new_grid[y][x+1]=grid[y][x+1]
                #         new_grid[y][x-1]=grid[y][x-1]
                #         new_grid[y-1][x]=grid[y-1][x]
                #         new_grid[y+1][x]=grid[y-1][x]
            if xmas:
                new_grid[y][x] = 'A'
                score+=1
    for line in new_grid:
        print("".join(line))
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
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

