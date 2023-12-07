import sys; sys.dont_write_bytecode = True; from util import *

card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J']
def hand_sort_key(hand_tuple):
    hand=hand_tuple[0]
    key = ''
    hand_dict = defaultdict(int)
    for c in hand:
        if c != 'J':
            hand_dict[c] +=1 
    sorted_by_freq = [i[0] for i in sorted(hand_dict.items(), key=operator.itemgetter(1), reverse=True)]

    hand_with_joker_replaced = hand.replace('J', sorted_by_freq[0]) if sorted_by_freq else hand
    hand_dict = defaultdict(int)
    for c in hand_with_joker_replaced:
        hand_dict[c] +=1
    sorted_by_freq = [i[1] for i in sorted(hand_dict.items(), key=operator.itemgetter(1), reverse=True)]

    key+=('0' if sorted_by_freq[0]==5 else '1') # five of a kind
    key+=('0' if sorted_by_freq[0]==4 else '1') # four of a kind
    key+=('0' if sorted_by_freq[0]==3 and len(hand_dict)==2 else '1') # full house
    key+=('0' if sorted_by_freq[0]==3 else '1') # 3 of a kind
    key+=('0' if sorted_by_freq[0]==2 and sorted_by_freq[1]==2 else '1') # two pair
    key+=('0' if sorted_by_freq[0]==2 else '1') # pair
    for c in hand:
        key+=(chr(97+card_order.index(c)))
    return key
    
    
        

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    score=0
    i = 0
    hands = []
    for y, line in enumerate(lines):
        hands.append((line.split()[0], int(line.split()[1])))

    hands = sorted(hands, key=hand_sort_key, reverse=True)
    score = 0
    for i, hand in enumerate(hands):
        score+= (i+1)*hand[1]
            
            

            
    print(hands)
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

