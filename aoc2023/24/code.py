import sys; sys.dont_write_bytecode = True; from util import *


def get_coords_one_below(block):
    coords = set()
    min_z = min(block[0][2], block[1][2])
    for x in range_smart_inclusive(block[0][0],block[1][0]):
        for y in range_smart_inclusive(block[0][1], block[1][1]):
            coords.add((x,y,min_z-1))
    return list(coords)

def get_coords(block):
    coords = set()
    max_z = max(block[0][2], block[1][2])
    for x in range_smart_inclusive(block[0][0],block[1][0]):
        for y in range_smart_inclusive(block[0][1], block[1][1]):
            coords.add((x,y,max_z))
    return list(coords)

class Hailstone:
    def __init__(self, x,y,z,dx,dy,dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz
    def __repr__(self):
        return "Hailstone(%s,%s,%s,%s,%s,%s)" % (self.x, self.y, self.z, self.dx, self.dy, self.dz)

def pairwise(iterable):
    for i, a in enumerate(iterable):
        for b in iterable[i+1:]:
            yield a, b 

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    
    MAX = 27
    MIN = 7
    lines = [row for row in inp.splitlines()]
    stones = []
    for l in lines:
        a,b = l.split("@")
        x,y,z = [float(foo.strip()) for foo in a.split(",")]
        dx,dy,dz = [float(foo.strip()) for foo in b.split(",")]
        stones.append(Hailstone(x,y,z,dx,dy,dz))
    
    score = 0 
    count=0
    for a,b in pairwise(stones):
        count+=1
        # x = x0 + t*dx
        # y = y0 + t*dy
        # t = (x-x0)/dx = (y-y0)/dy
        # and
        # ya = ya0 + t*dya
        # yb = yb0 + t*dyb
        # solve for yb0 + t*dyb = ya0 + t*dya
        # yb0 - ya0 = t*dya - t*dyb
        # yb0 - ya0 = t(dya - dyb)
        # t = (yb0 - ya0)/(dya - dyb)
        # if (a.dx - b.dx) == 0:
        #     # print("parallel", a,b)
        #     continue
        # t = (b.x - a.x)/(a.dx - b.dx)
        # y_int = a.y + t*a.dy
        # x_int = a.x + t*a.dx

        # if t>0 and y_int>=MIN and y_int<=MAX and x_int>=MIN and x_int<=MAX:
        #     # print("intersection",x_int, y_int, t, a,b)
        #     score+=1

        # actually we don't care about intersection at the same moment in time, just that the paths cross
        # so what we want is yb0+t1*dyb = ya0+t2*dya
        # and  xa0 + t1*dax = xb0 + t2*dbx
        # solve for t1 and t2
        # t1 = (ya0 - yb0 + t2*dyb)/dyb
        # t2 = (xa0 - xb0 + t1*dax)/dbx
        # actually t is irrelevant here
        # y = ya0 + xdy
        # y = yb0 + dy
        # t1 = (b.y - a.y + t2*b.dy)/b.dy
        # t2 = (a.x - b.x + t1*a.dx)/a.dx

        #actually actually, times are not relevant -- we just want to see if lines cross at all in the area (for part 1 at least)
        #for a:
        # ya = ya0+dya/dxa*(x-xa0)
        # yb = yb0+dyb/dxb*(x-xb0)
        # so at intersection, for some x:
        # ya0+dya/dxa*(x-xa0) = yb0+dyb/dxb*(x-xb0)
        # ya0+dya/dxa*x-dya/dxa*xa0 = yb0+dyb/dxb*x-dyb/dxb*xb0
        # ya0-dya/dxa*xa0 = yb0-dyb/dxb*xb0 + (dyb/dxb-dya/dxa)*x
        # ya0-dya/dxa*xa0 = yb0-dyb/dxb*xb0 + (dyb/dxb-dya/dxa)*x
        # x = (ya0-dya/dxa*xa0 - yb0+dyb/dxb*xb0)/(dyb/dxb-dya/dxa)
        if (a.dx - b.dx) == 0 and (a.dy - b.dy) == 0:
            print("parallel", a,b)
            continue
        if a.dx == 0 or b.dx == 0 or (b.dy/b.dx - a.dy/a.dx) == 0:
            print("???", a,b)
            continue
        x = (a.y - a.dy/a.dx*a.x - b.y + b.dy/b.dx*b.x)/(b.dy/b.dx - a.dy/a.dx)
        y = a.y + a.dy/a.dx*(x-a.x)
        if x>=MIN and x<=MAX and y>=MIN and y<=MAX:
            # now check time
            ta = (x-a.x)/a.dx
            tb = (x-b.x)/b.dx
            if ta>0 and tb>0:
                score+=1
            print("intersection",x, y, a,b) 
            


    print("Part 1", score)

            
    # we need to find x,y,z and dx,dy,dz such that we hit all the stones
    # x,y,z,dx,dy,dz are all integers
    # and we can hit hailstone at different times
    # for each hailstone h, there exists a t such that:
    # h.x + t*h.dx= x + t*dx (same for y and z, and t>0)

    # we know a solution exists, so maybe we can construct enough equations to solve our unknowns
    # each axis is fully independent? (no - the t's connect)
    
    # h.x + t*h.dx= x + t*dx 
    # t*(h.dx-dx) = x-h.x
    # t = (x-h.x)/(h.dx-dx)
    # t = (y-h.y)/(h.dy-dy)
    # so (x-h.x)(h.dy-dy) = (y-h.y)(h.dx-dx)
    
    # (for every hailstone)
    # 4 unknowns

    for h in stones:
        print(f"({h.x} - x) * ({h.dy} - dy) = ({h.y} - y) * ({h.dx} - dx)")
        print(f"x*dy -y*dx +{h.y}dx + {h.dx}x - {h.x}dy -{h.dy}y = {h.y*h.dx-h.x*h.dy}")
        

        

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
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

