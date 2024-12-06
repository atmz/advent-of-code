import sys; sys.dont_write_bytecode = True; from util import *

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    score=0
    score2=0
    symbols = defaultdict(str )
    gears = defaultdict(list )
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if not c.isdigit() and c!=".":
                symbols[(y,x)] = c
    for y, line in enumerate(lines):
        num=''
        part = 0
        seenstars=set()
        for x, c in enumerate(line):
            if c.isdigit():
                num+=c
                for a in range(y-1,y+2):
                    for b in range(x-1,x+2):
                        if symbols[(a,b)]:
                            part+=1
                            if symbols[(a,b)] == "*":
                                seenstars.add((a,b))
            else:
                if(part):
                    score+=int(num)
                    if seenstars:
                        for star in seenstars:
                            gears[star].append(int(num))
                num=''
                part=0
                seenstars=set()
        if(part):
            score+=int(num)
            if seenstars:
                for star in seenstars:
                    gears[star].append(int(num))
    
    for star in gears:
        # print(star)
        if len(gears[star])==2:
            score2+= gears[star][0]*gears[star][1]

    print(score)
    print(gears)
    print(score2)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
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

