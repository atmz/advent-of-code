import sys; sys.dont_write_bytecode = True; from util import *
from sympy import Matrix, solve_linear_system
from sympy.abc import m, n

class Game:
    def __init__(self, lines):
        a = lines[0].split(':')[1]
        b = lines[1].split(':')[1]
        prize = lines[2].split(':')[1]
        self.ax = int(a.split(',')[0].split('+')[1])
        self.ay = int(a.split(',')[1].split('+')[1])
        self.bx = int(b.split(',')[0].split('+')[1])
        self.by = int(b.split(',')[1].split('+')[1])
        self.prizex = int(prize.split(',')[0].split('=')[1])+10000000000000
        self.prizey = int(prize.split(',')[1].split('=')[1])+10000000000000

    def __str__(self):
        return f"{self.ax} {self.ay} {self.bx} {self.by} {self.prizex} {self.prizey}"

    def solve_naive(self, max_it=10000000000000):
        best = 0
        print(self)
        max_a = self.prizex // self.ax
        for i in range (max_a,0,-1):
            # try to solve for prizex
            x = self.ax *i
            bx = self.prizex - x
            if bx>0 and bx % self.bx == 0:
                a_presses = i
                b_presses = bx // self.bx
                # print("match for x:", a_presses, b_presses)
                if a_presses <= max_it and b_presses <= max_it:
                    #now check Y
                    if (b_presses * self.by + a_presses * self.ay) == self.prizey:
                        coins = 3*a_presses + b_presses
                        if best==0 or coins<best:
                            best=coins
                            # print("new best",best, a_presses,b_presses)
        return best
    
    def solve_medium(self):
        # We want to find the solution that costs the minimum coins
        # in some cases, this maximises b presses, in some it maximizes a presses
        # a presses cost 3 though, so let's try to just maximize b presses
        #
        # Starting at prizes, subtract a presses until we get to a number that is divisible
        # by ax and bx
        print(self)
        score_favoring_a=None
        score_favoring_b=None
        px = self.prizex
        py =self.prizey
        a_presses = 0
        while (
            px>=self.ax and py>=self.ay
            and (
                px % self.bx != 0 or py % self.by != 0
                or px // self.bx != py // self.by)
        ):
            px-=self.ax
            py-=self.ay
            a_presses+=1
        
        b_presses = px // self.bx
        if px>=0 and py>=0 and px % self.bx == 0 and py % self.by == 0:
            print("score_favoring_b", a_presses, b_presses)
            score_favoring_b =  a_presses*3 + b_presses

        px = self.prizex
        py =self.prizey
        b_presses = 0
        while (
            px>=self.bx and py>=self.by
            and (
                px % self.ax != 0 or py % self.ay != 0
                or px // self.ax != py // self.ay)
        ):
            px-=self.bx
            py-=self.by
            b_presses+=1
        
        a_presses = px // self.ax
        if px>=0 and py>=0 and px % self.ax == 0 and py % self.ay == 0:
            score_favoring_a =  a_presses*3 + b_presses
            print("score_favoring_a", a_presses, b_presses)

        if score_favoring_a and score_favoring_b:
            return min(score_favoring_a, score_favoring_b)
        elif score_favoring_a:
            return score_favoring_a
        elif score_favoring_b:
            return score_favoring_b
        return 0
        
        # now we have a number that is divisible by both ax and bx




    def solve_fast(self):
        # We are trying to solve - find m and n such that:
        # ax * m + bx * n = prizex
        # ay * m + by * n = prizey
        system = Matrix((
                (self.ax, self.bx, self.prizex),
                (self.ay, self.by, self.prizey)
        ))
        solutions = solve_linear_system(system, m,n)
        if m in solutions and n in solutions:
            if solutions[m].is_integer and solutions[n].is_integer:
                return 3*solutions[m] + solutions[n]
        print(solutions)
        return 0



def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    score=0
    for i in range(0, len(lines)-2, 4):
        x = lines[i].split()
        y = lines[i+1].split()
        g = Game(lines[i:i+3])
        score+=g.solve_fast()
    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD




run_samples_and_actual([
# Part 1
r"""Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""",
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

