import sys; sys.dont_write_bytecode = True; from util import *


def get_next(sequence):
    diffs = []
    diff = []
    diff=sequence
    diffs.append(diff)
    while len(set(diff))!=1 or diff[0]==0:
        newdiff = []
        for i,n in enumerate(diff[1:]):
            newdiff.append(n-diff[i])
        diff = newdiff
        diffs.append(diff)
    next = 0
    diffs.reverse()
    for i,n in enumerate(diffs[:-1]):
        diffs[i+1].insert(0,(diffs[i+1][0]-diffs[i][0]))
    # for diff in diffs:
    #     print(diff)
    # print("next",diffs[-1][-1] )
    return diffs[-1][0]



def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    defaultdict_int = defaultdict(int)

    score=0
    for i, line in enumerate(lines):
        if line:
            score+=get_next([int(i) for i in line.split()])
            pass


    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
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

