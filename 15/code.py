import sys; sys.dont_write_bytecode = True; from util import *

def hash(string):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value = value % 256
    return value




def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    score=0
    for line in lines:
        for ins in line.split(','):
            score+=hash(ins)
    print("Part 1")
    print(score)
    score=0
    values = {}
    boxes = [[] for i in range(0,256)]
    for line in lines:
        for ins in line.split(','):
            if '=' in ins:
                label, focal = ins.split('=')
                box = hash(label)
                focal = int(focal)
                if label not in boxes[box]:
                    boxes[box].append(label)
                values[label] = focal
            elif '-' in ins:
                label = ins.strip('-')
                box = hash(label)
                if label in boxes[box]:
                    boxes[box].remove(label)
    
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            score += (i+1) * (j+1) * values[lens]
    
    print("Part 2")
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
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

