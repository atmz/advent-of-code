import sys; sys.dont_write_bytecode = True; from util import *

card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def hand_comparator(tuple_a,tuple_b):
    a = tuple_a[0]
    b = tuple_b[0]
    if len(set(a))>len(set(b)):
        return -1
    elif len(set(a))<len(set(b)):
        return 1
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)
    for c in a:
        a_dict[c] +=1
    for c in b:
        b_dict[c] +=1
    if max(a_dict.values())>max(b_dict.values()):
        return 1
    if max(a_dict.values())<max(b_dict.values()):
        return -1

    for i in range(0,5):
        if a[i]!=b[i]:
            if card_order.index(a[i]) < card_order.index(b[i]):
                return 1
            return -1
    return 0



def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    instructions = lines[0]
    instructions = 'L'*276+'R'
    print(len(instructions))
    pointer=0
    currents =[]
    last_match = []
    periods = []
    firsts = []
    #load data
    score=0
    rows = {}
    goal = 'ZZZ'
    for i, line in enumerate(lines[1:]):
        if line:
            a,b= line.split('=')
            rows[a.strip()] = [x.strip() for x in (b.strip(' ()').split(','))]
            if a.strip()[-1] == 'A': # Part 2
            #if a.strip() == 'AAA': # Part 1
                currents.append(a.strip())
                last_match.append(0)
                periods.append(0)
                firsts.append(0)
            
        pass
    print(currents)

    def iswin(currents):
        return False# Part 2
        #return 'ZZZ' in currents # Part 1
    current = 'AAA'
    while not iswin(currents):
        score+=1
        if pointer>=len(instructions):
            pointer=0
        if instructions[pointer] == 'R':
            for i,a in enumerate(currents):
                currents[i] = rows[a][1]
        elif instructions[pointer] == 'L':
            for i,a in enumerate(currents):
                currents[i] = rows[a][0]
        matches = [i for i,a in enumerate(currents) if a[-1]=='Z']
        if matches:
            for m in matches:
                if last_match[m]!=0:
                    periods[m] = score-last_match[m] 
                last_match[m] = score
                if firsts[m]==0:
                    firsts[m]=score
            if not any([p==0 for p in periods]):
                break
        pointer+=1


    print(math.lcm(*periods))
    print(len(instructions), periods)
    print(math.gcd(*periods))

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
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

