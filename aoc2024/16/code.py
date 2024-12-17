
import sys; sys.dont_write_bytecode = True; from util import *

class PriorityQueue:
    def __init__(self):
        self.seen = {}
        self.done = set()
    def push(self, k,v):
        (pos, d) = k
        (score,path) = v
        # path = str(path)
        if (pos,d) in self.done:
            return
        if (pos,d) in self.seen:
            other_score, other_path = self.seen[(pos,d)]
            if score>other_score:
                return
            if score<other_score:
                self.seen[(pos,d)]= (score,path)
            if score == other_score:
                self.seen[(pos,d)]= (score,path+other_path)
        else:
            self.seen[(pos,d)] = (score, path)
    def pop(self):
        key = min(self.seen, key=lambda k: self.seen[k][0])
        value = self.seen.pop(key)
        self.done.add(key)
        return (key[0], key[1]), (value[0],value[1])
    
    def __len__(self):
        return len(self.seen)
    def __str__(self):
        return str(self.seen)


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid=[]
    for line in lines:
        grid.append([c for c in line])
        print(line)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (x,y)
            if grid[y][x] == "E":
                end = (x,y)
    pq = PriorityQueue()
    pq.push((start, (1,0)), (0,[start]))
    on_a_best_path = set()
    best = None


    while len(pq):
        (pos, dir), (score,path) = pq.pop()
        if len(path) % 10 == 0:
            print((pos, dir), (score,len(path)))
        if pos == end:
            if not best:
                print("Part 1:", score)
                best = score
            if score > best:
                print("Part 2:", len(on_a_best_path))
                return
            else:
                print("another path")
            on_a_best_path=on_a_best_path.union(set(path))
        else:
            for d in [(0,1), (0,-1), (1,0), (-1,0)]:
                if d[0]!=-dir[0] or d[1]!=-dir[1]:
                    new_score = score+1
                    new_pos = (pos[0]+d[0], pos[1]+d[1])
                    if dir!=d:
                        new_score+=1000
                    if grid[new_pos[1]][new_pos[0]] != "#":
                        new_path=deepcopy(path)
                        new_path.append(new_pos)
                        pq.push((new_pos, d), (new_score,new_path))
                        # print("added",(new_pos, d), (new_score+1,new_path))

    
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################

"""
,r"""

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

