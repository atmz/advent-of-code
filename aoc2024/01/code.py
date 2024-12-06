import sys; sys.dont_write_bytecode = True; from util import *


            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    list_a = []
    list_b = []
    counts_b = defaultdict(int)
    for line in lines:
        a,b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))
        counts_b[int(b)]+=1
    score=0
    score_2=0
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    for i, _ in enumerate(list_a):
        score+= abs(list_a[i]-list_b[i])
        score_2+= list_a[i] * counts_b[list_a[i] ]
    print("Part 1", score)
    print("Part 2", score_2)




    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""3   4
4   3
2   5
1   3
3   9
3   3
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

