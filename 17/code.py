import sys; sys.dont_write_bytecode = True; from util import *
from  heapq import heappush, heappop



def opposite_direction(d):
    if d == '<':
        return '>'
    if d == '>':
        return '<'
    if d == '^':
        return 'v'
    if d == 'v':
        return '^'
    
def valid_coords(x,y,grid):
    if x<0:
        return False
    if y<0:
        return False
    if x>=len(grid[0]):
        return False
    if y>=len(grid):
        return False
    return True

def do_move(x,y,d):
    if d == '<':
        return x-1, y
    if d == '>':
        return x+1, y
    if d == '^':
        return x, y-1
    if d == 'v':
        return x, y+1

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)

    # Part 1
    lines = inp.splitlines()
    grid = [list(x) for x in lines]
    seen = {}
    best = 999999
    heap = []
    heappush(heap, (0,0,0,'   '))
    # print_grid(grid)
    while heap:
        #print(seen)
        state=heappop(heap)
        # print(state)
        score, x,y,path = state
        # print(queue)
        seen[(x,y,path[-3:])]=score
        if score>best:
            break
        if x == len(grid[0])-1 and y == len(grid)-1:
            if best>score:
                best=score
                print(f"best so far:{score}")
                print(f"path: {path}")
        else:
            for d in ['<','>','^', 'v']:
                new_x,new_y = do_move(x,y,d)
                if (
                    valid_coords(new_x,new_y,grid) 
                    and not path.endswith(d*3) 
                    and path[-1]!=opposite_direction(d)
                    and score<best
                ):
                    new_score = score + int(grid[new_y][new_x])
                    new_path =path[-2:]+d
                    if ( new_score < best and
                        (
                        (new_x,new_y,new_path ) not in seen
                        or seen[(new_x,new_y,new_path )]>new_score)
                    ):
                        seen[(new_x,new_y,new_path )]=new_score
                        heappush(heap, (new_score, new_x,new_y,new_path) )
    
    #print(seen)
    print(f"Part 1: {best}")
    # Part 2
    seen = {}
    best = 999999
    heap = []
    heappush(heap, (0,0,0,'   '))
    # print_grid(grid)
    while heap:
        #print(seen)
        state=heappop(heap)
        score, x,y,path = state
        # print(queue)
        seen[(x,y,path[-10:])]=score
        if x == len(grid[0])-1 and y == len(grid)-1 and path.endswith(path[-1]*4):
            best=score
            print(f"path: {path}")
            break
        else:
            for d in ['<','>','^', 'v']:
                new_x,new_y = do_move(x,y,d)
                if (
                    valid_coords(new_x,new_y,grid) 
                    and not path== d*10 
                    and (d==path[-1] or path.endswith(path[-1]*4) or path[-1]==' ')
                    and path[-1]!=opposite_direction(d)
                    and score<best
                ):
                    new_score = score + int(grid[new_y][new_x])
                    new_path =path[-9:]+d
                    if ( new_score < best and
                        (
                        (new_x,new_y,new_path ) not in seen
                        or seen[(new_x,new_y,new_path )]>new_score)
                    ):
                        seen[(new_x,new_y,new_path )]=new_score
                        heappush(heap, (new_score, new_x,new_y,new_path) )
    
    #print(seen)
    print(f"Part 2: {best}")



                


    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
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

