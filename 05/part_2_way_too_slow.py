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
def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    #load data
    score=0
    score2=0
    i = 0
    seeds = set()
    seen = set()
    source=''
    a=0
    b=0
    for y, line in enumerate(lines):
        if line:
            bits = line.split(':')
            if line.strip().endswith(':'):
                bits = line.split()[0].split('-')
                for k in list(seeds):
                    if k[0]==source and k not in seen:
                        seeds.add((dest,k[1]))
                print(seeds)
                seen = set()
                source = bits[0]
                dest = bits[2]
                    
                
            elif len(bits) == 2:
                foo =bits[1].split()
                print(foo)
                for i,v in enumerate(bits[1].split()):
                    if i %2 == 0:
                        for v in range(int(foo[i]), int(foo[i])+int(foo[i+1])):
                            seeds.add(("seed",v))
                        print(seeds)
                print(seeds)
            elif len(bits) == 1:
                    a,b,c=line.split()
                    a = int(a)
                    b = int(b)
                    c = int(c)
                    for k in list(seeds):
                        if k[0]==source and k[1]>=b and k[1]<b+c:
                            seeds.add( (dest,a+(k[1]-b) ))
                            seen.add(k)


                    # for i in range(0, c):
                    #     if (source,b+i) in seeds:
                    #         seeds.add((dest,a+i))
                    #         seen.add((source,b+i))
    
    for k in list(seeds):
        if k[0]==source and k not in seen:
            seeds.add((dest,k[1]))
    print(seeds)

    print( min([k for k in list(seeds) if k[0]=="location"], key = lambda k: k[1]  ))


                
            
    
    print(score)
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

