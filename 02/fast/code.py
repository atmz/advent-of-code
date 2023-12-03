import sys; sys.dont_write_bytecode = True; from util import *

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    score=0
    for line in lines:
        if line:
            split = line.split(':')
            possible = 1
            r=0
            g=0
            b=0
            for game in split[1].split(";"):
                print(game)
                tr=0
                tg=0
                tb=0
                for word in game.split(","):
                    print(word.split())
                    c,col = word.split()
                    if col == "red":
                        tr+=int(c)
                    if col == "blue":
                        tb+=int(c)
                    if col == "green":
                        tg+=int(c)
                r=max(r,tr)
                b=max(b,tb)
                g=max(g,tg)
            power = r*b*g
            score+= power
            print(line, possible)
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

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

