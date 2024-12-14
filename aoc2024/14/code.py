import sys; sys.dont_write_bytecode = True; from util import *
from sympy import Matrix, solve_linear_system
from sympy.abc import m, n

class Robot:
    def __init__(self, line, grid_x,grid_y):
        # e.g. p=0,4 v=3,-3
        self.px,self.py = [int(i) for i in line.split(' ')[0].split('=')[1].split(',')]
        self.vx,self.vy = [int(i) for i in line.split(' ')[1].split('=')[1].split(',')]
        self.grid_x = grid_x
        self.grid_y = grid_y

    def pos_at_step(self, step):
        x = (self.px + self.vx*step) % self.grid_x
        y = (self.py + self.vy*step) % self.grid_y
        return x,y

    def quadrant_at_step(self, step):
        x,y = self.pos_at_step(step)
        if x < (self.grid_x-1)//2:
            if y < (self.grid_y-1)//2:
                return 1
            elif y > (self.grid_y-1)//2:
                return 2
        elif x > (self.grid_x-1)//2:
            if y < (self.grid_y-1)//2:
                return 3
            elif y > (self.grid_y-1)//2:
                return 4
        print("No quadrant found for", x,y, "at step", step)
        return None



def xmas_tree_score(pos):
    # what does an xmas tree look like?
    #       #
    #      ###
    #     #####
    #    #######
    best = 0
    for x,y in pos:
        score=0
        try:
            level = 0
            while (x,y+level+1) in pos.keys():
                level+=1
                for i in range(-level,level):
                    if not (x+i,y+level) in pos.keys():
                        break
                    score+=1
        except IndexError:
            pass
        if score>best:
            best=score

    return(best)

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    grid_x = 101
    grid_y = 103
    lines = inp.splitlines()
    quadrants = defaultdict(int)
    pos = defaultdict(int)
    for line in lines:
        r = Robot(line, grid_x,grid_y)
        q = r.quadrant_at_step(100)
        if q:
            quadrants[q] += 1
            pos[r.pos_at_step(100)]+=1
    print(quadrants)
    print(sum(quadrants.values()))
    print(len(lines))
    print(math.prod(quadrants.values()))
    # for i in range(0,grid_y):
    #     line = "".join([ 
    #         str(pos[(j,i)]) 
    #         if pos[(j,i)] else (
    #              ' ' if j == (grid_x-1)//2 or i == (grid_y-1)//2
    #             else
    #                 '.'            )
             
    #           for j in range(0,grid_x)])
    #     print(line)
    for s in range(0,100000):
        pos = defaultdict(int)
        for line in lines:
            r = Robot(line, grid_x,grid_y)
            pos[r.pos_at_step(s)]+=1
        
        # for i in range(0,grid_y):
        #     line = "".join([ 
        #         '#' if pos[(j,i)] else '.'  for j in range(0,grid_x)])
        #     print(line)
        score = xmas_tree_score(pos)
        if score >25:
            print(s, score)
            for i in range(0,grid_y):
                line = "".join([ 
                    '#' if pos[(j,i)] else '.'  for j in range(0,grid_x)])
                print(line)
        

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD




run_samples_and_actual([
# Part 1
r"""p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""",
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

