import sys; sys.dont_write_bytecode = True; from util import *



def get_vertical(pattern, score_to_ignore=0):
    transposed = [
        ''.join([x[i] for x in pattern])
        for i in range(0, len(pattern[0]))
    ]
    # print_grid(pattern)
    # print_grid(transposed)
    for x, _ in enumerate(transposed):
        if  x+1<len(transposed):
            mirror = True
            for i in range(0,x+1):
                if (i+x+1)<len(transposed):
                    if transposed[x-i] != transposed[x+i+1]:
                        mirror = False
                        break
            if mirror:
                print(f"vertical mirror at {x+1}")
                if x+1 != score_to_ignore:
                    return (x+1)
    return 0

def get_horizontal(pattern, score_to_ignore=0):
    for y, _ in enumerate(pattern):
        # print(f"y={y}")
        if  y+1<len(pattern):
            mirror = True
            for i in range(0,y+1):
                # print(i)
                if (i+y+1)<len(pattern):
                    # print( pattern[y-i], pattern[y+i+1])
                    if pattern[y-i] != pattern[y+i+1]:
                        mirror = False
                        break
            if mirror:
                print(f"horizontal mirror at {y+1}")
                if (y+1)*100 != score_to_ignore:
                    return (y+1)*100

    return 0

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()


    
    score = 0
    patterns = []
    pattern = []
    for line in lines:
        if line!='':
            pattern.append(list(line.replace("."," ").replace("O","○").replace("#","█")))
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)

    for pattern in patterns:
        horizontal = 0
        vertical = 0
        horizontal = get_horizontal(pattern)
        if not horizontal:
            vertical = get_vertical(pattern)
        if (horizontal+vertical) ==0:
            print_grid(pattern)
            print("\n")

        score += horizontal
        score += vertical
        

    print(f"Part 1: {score}")


    score = 0
    for pattern in patterns:
        horizontal = 0
        vertical = 0
        horizontal = get_horizontal(pattern)
        if not horizontal:
            vertical = get_vertical(pattern)
        if (horizontal+vertical) ==0:
            print_grid(pattern)
            print("\n")

        score_to_ignore = horizontal+vertical
        
        horizontal = 0
        vertical = 0

        x=0
        y=0
        
        while (horizontal+vertical)==0:
            if pattern[y][x] == '█':
                pattern[y][x]= ' '
            else:
                pattern[y][x]= '█'

            horizontal = get_horizontal(pattern,score_to_ignore)
            if not horizontal:
                vertical = get_vertical(pattern,score_to_ignore)

            if pattern[y][x] == '█':
                pattern[y][x]= ' '
            else:
                pattern[y][x]= '█'
            if x<len(pattern[0])-1:
                x+=1
            else:
                x=0
                y+=1
        
        score += horizontal
        score += vertical
    
    print(f"Part 2: {score}")


    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
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

