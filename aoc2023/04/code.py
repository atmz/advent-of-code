import sys; sys.dont_write_bytecode = True; from util import *

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    cards = []
    cards_dict={}
    i = 0
    for y, line in enumerate(lines):
        if line:
            lucky, mine = line.split("|")
            luckynum = set()
            mine_list = list()
            print(lucky)
            for n in lucky.split(':')[1].split():
                luckynum.add(n)
            for n in mine.split():
                mine_list.append(n)
            num = lucky.split(':')[0].split()[1]
            cards.append((luckynum,mine_list, int(num)))
            cards_dict[int(num)] = (luckynum,mine_list, int(num))
    while i<len(cards):
        lucky = 0
        for n in cards[i][1]:
            if n in cards[i][0]:
                lucky+=1
        for x in range(0,lucky):
            cards.insert(i+x+1,cards_dict[cards[i][2]+x+1])
        i+=1
      
    print(len(cards)) # Part 2
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
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
