import sys; sys.dont_write_bytecode = True; from util import *

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    score=1
    times = [int(i) for i in lines[0].split(':')[1].split()]
    distances = [int(i) for i in lines[1].split(':')[1].split()]
    for i, time in enumerate(times):
        score_time = 0
        distance = distances[i]
        for t in range(1,time):
            speed = t 
            time_taken = distance/speed + t
            if time_taken<time:
                score_time+=1
        score*=score_time
    
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
Part 1: Time:        34     90     89     86
Distance:   204   1713   1210   1780
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
Part 1: Time:        34908986
Distance:   204171312101780

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)

