import sys; sys.dont_write_bytecode = True; from util import *


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    score=0
    for line in lines:
        l=line
        l=l.replace("one",'o1e')
        l=l.replace("two", 't2o')
        l=l.replace("three", 'th3ee')
        l=l.replace("four", 'f4ur')
        l=l.replace("five", 'f5ve')
        l=l.replace("six", '6ix')
        l=l.replace("seven", '7even')
        l=l.replace("eight", 'ei8ht')
        l=l.replace("nine", 'ni9e')
        
        l = [c for c in l if c.isnumeric()]
        print(line,l,l[0]+l[-1] )
        score+= int(l[0]+l[-1])
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

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

