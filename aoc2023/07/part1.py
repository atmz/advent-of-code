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

    #load data
    score=0
    i = 0
    hands = []
    for y, line in enumerate(lines):
        hands.append((line.split()[0], int(line.split()[1])))

    hands = sorted(hands, key=functools.cmp_to_key(hand_comparator))
    score = 0
    for i, hand in enumerate(hands):
        score+= (i+1)*hand[1]
            
            

            
    
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
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

