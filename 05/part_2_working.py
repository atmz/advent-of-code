import sys; sys.dont_write_bytecode = True; from util import *
"""
To do: ensure Code Runner works (in WSL), have preloaded the day and input in Chrome,
saved input into the folder, have utils on the side, collapse regions
Strings, lists, dicts:
lmap, ints, positive_ints, floats, positive_floats, words, keyvalues

Algorithms:
bisect, binary_search, hamming_distance, edit_distance

Data structures:
Linked, UnionFind
use deque for queue: q[0], q.append and q.popleft

List/Vector operations:
GRID_DELTA, OCT_DELTA
lget, lset, fst, snd
padd, pneg, psub, pmul, pdot, pdist1, pdist2sq, pdist2

Matrices:
matmat, matvec, matexp

Previous problems:
knot

Dict things:
dict.keys()
dict.values()
dict.items()
"""

class Seed:
    def __init__(self, type, start, end):
        self.type = type
        self.start = start
        self.end = end #exclusive

    def print(self):
        print(f"{self.type}: {self.start}-{self.end}")

    def is_valid(self):
        return self.end>self.start

    def get_overlap_and_remainder(self, map_start, map_end, new_type, delta):
        if self.type==new_type:
            return [self]
        overlap = (max(map_start,self.start), min(map_end, self.end))
        if overlap[1]<=overlap[0]:
            return [self] #No overlap
        potential_seeds = [
            Seed(self.type, self.start,overlap[0]),            # remainder before
            Seed(new_type,overlap[0]+delta,overlap[1]+delta),            # overlap
            Seed(self.type, overlap[1],self.end),            # remainder after
        ]
        return [s for s in potential_seeds if s.is_valid()]

    def convert_type(self, new_type):
        self.type = new_type
        
def convert_remaining(seeds, new_type):
    for s in seeds:
        s.convert_type(new_type)

def convert(seeds, new_type, overlap_start, overlap_end, delta):
    new_seeds = []
    for s in seeds:
        new_seeds.extend(s.get_overlap_and_remainder(overlap_start, overlap_end,new_type, delta))
    print("### before")
    print_seeds(seeds)
    print("### after")
    print_seeds(new_seeds)
    return new_seeds
        
def print_seeds(seeds):
    for s in seeds:
        s.print()


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    seeds = []
    current_type="seed"
    for y, line in enumerate(lines):
        if line:
            bits = line.split(':')
            if line.strip().endswith(':'):
                bits = line.split()[0].split('-')
                convert_remaining(seeds, current_type)
                seen = set()
                current_type = bits[2]
                print_seeds(seeds)
                    
            #initial setup
            elif len(bits) == 2:
                foo =bits[1].split()
                for i,v in enumerate(bits[1].split()):
                    if i %2 == 0:
                        seeds.append(Seed('seed', int(foo[i]), int(foo[i])+int(foo[i+1])))
                print_seeds(seeds)
            elif len(bits) == 1:
                    a,b,c=line.split()
                    dest_start = int(a)
                    source_start = int(b)
                    length = int(c)
                    source_end = source_start+length
                    delta = dest_start-source_start
                    print(source_start, source_end, delta)
                    seeds = convert(seeds, current_type, source_start, source_end, delta)


                    # for i in range(0, c):
                    #     if (source,b+i) in seeds:
                    #         seeds.add((dest,a+i))
                    #         seen.add((source,b+i))
    

    convert_remaining(seeds, current_type)
    print("final state")
    print_seeds(seeds)
    min([k for k in seeds if k.type=="location"], key = lambda k: k.start  ).print()

            
    
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
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

