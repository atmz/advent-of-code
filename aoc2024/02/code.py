import sys; sys.dont_write_bytecode = True; from util import *


            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    score = 0
    for line in lines:
        levels = line.split()
        last_diff = None
        last =  None
        success = True
        for l in levels:
            i = int(l.strip())
            if last_diff:
                if last_diff * (i-last) < 0:
                    success = False
                    break
            if last:
                if abs(i-last)>3 or i==last:
                    success = False
                    break
                last_diff = i-last
            last = i
        if success:
            print(line)
            score+=1
    print("Part 1", score)
    lines = inp.splitlines()
    score = 0
    for line in lines:
        levels = line.split()
        fail_count = 0
        for index_to_ignore in range(0, len(levels)):
            last_diff = None
            last =  None
            for index, l in enumerate(levels):
                if index != index_to_ignore:
                    i = int(l.strip())
                    if last_diff:
                        if last_diff * (i-last) < 0:
                            fail_count+=1
                            break
                    if last:
                        if abs(i-last)>3 or i==last:
                            fail_count+=1
                            break
                        last_diff = i-last
                    last = i
        if fail_count<len(levels):
            score+=1
        print(line, fail_count)
    print("Part 2", score)






    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
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

