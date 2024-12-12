import sys; sys.dont_write_bytecode = True; from util import *

class RockLine:
    def __init__(self, rocks):
        self.rocks = defaultdict(int)
        for i, rock in enumerate(rocks):
            self.rocks[rock]+=1
        self.iterations = 0

    def count(self):
        return sum(self.rocks.values())

    def iterate(self):
        new_rocks = defaultdict(int)
        for rock, count in self.rocks.items():
            if rock == 0:
                new_rocks[1]+=count
            elif len(str(rock)) % 2 == 0:
                new_rocks[int(str(rock)[:len(str(rock))//2])]+=count
                new_rocks[int(str(rock)[len(str(rock))//2:])]+=count
            else:
                new_rocks[rock*2024]+=count
        self.rocks = new_rocks
    
    def calculate(self,i):
        for x in range(1,i+1):
            self.iterate()
            print(i, self.count())

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    rl = RockLine([int(i) for i in lines[0].split()])
    rl.calculate(75)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


#part_1 - same as part 2 but slow
def iterate(rocks):
    new_rocks = []
    for rock in rocks:
        if rock == 0:
            new_rocks.append(1)
        elif len(str(rock)) % 2 == 0:
            new_rocks.append(int(str(rock)[:len(str(rock))//2]))
            new_rocks.append(int(str(rock)[len(str(rock))//2:]))
        else:
            new_rocks.append(rock*2024)
    return new_rocks
def part_1(input):
    lines = input.splitlines()
    rocks = [int(i) for i in lines[0].split()]

    for i in range(1,26):
        rocks = iterate(rocks)
        print(i, len(rocks))
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""125 17""",
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

