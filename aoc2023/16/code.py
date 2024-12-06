import sys; sys.dont_write_bytecode = True; from util import *

def calcuate(grid, starting_state):
        state = starting_state
        grid_with_laser = deepcopy(grid)
        for y,row in enumerate(grid_with_laser):
            for x, c in enumerate(row):
                if c == '.':
                    grid_with_laser[y][x]=' '
        energized = deepcopy(grid)
        seen = set()
        
        while state:
            # print(state)
            # print(seen)
            # print_grid(grid_with_laser)
            new_state=[]
            for s in state:
                (x,y,d) = s
                if d == '>':
                    x+=1
                elif d == '<':
                    x-=1
                elif d == '^':
                    y-=1
                elif d == 'v':
                    y+=1
                # print(f" d:{d} x:{x} y:{y}")
                # out of bounds, gone forever
                if y >= len(grid) or y<0:
                    continue
                if x >= len(grid[0]) or x<0:
                    continue
                energized[y][x] = '#'
                operation = grid[y][x]
                # print(f"op:{operation} d:{d} x:{x} y:{y}")
                if operation == '\\':
                    if d == '>':
                        d = 'v'
                    elif d == '<':
                        d = '^'
                    elif d == '^':
                        d = '<'
                    elif d == 'v':
                        d = '>'
                if operation == '/':
                    if d == '>':
                        d = '^'
                    elif d == '<':
                        d = 'v'
                    elif d == '^':
                        d = '>'
                    elif d == 'v':
                        d = '<'
                if operation == '|' and d in ['>','<']:
                    new_state.append((x,y,'^'))
                    new_state.append((x,y,'v'))
                elif operation == '-' and d in ['^','v']:
                    new_state.append((x,y,'<'))
                    new_state.append((x,y,'>'))
                else:
                    new_state.append((x,y,d))
                    if operation =='.':
                        grid_with_laser[y][x] = d
                # print(f"op:{operation} newd:{d} x:{x} y:{y}")
            state = [s for s in new_state if s not in seen]
            for s in state:
                seen.add(s)
        # print(seen)
        # print_grid(grid_with_laser)
        # print_grid(energized)
        # print(len(set(
        #     [(x,y) for (x,y,z) in seen]
        # )))
        return len(set(
            [(x,y) for (x,y,z) in seen]
        ))


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid = [list(x) for x in lines]
    best = calcuate(grid, [(-1,0,'>')])
    print(f"Part 1 - {best}")
    for x in range(0,len(grid[0])):
        best = max(best, calcuate(grid, [(x,-1,'v')]))
        best = max(best, calcuate(grid, [(x,len(grid),'^')]))
    for y in range(0,len(grid)):
        best = max(best, calcuate(grid, [(-1,y,'>')]))
        best = max(best, calcuate(grid, [(len(grid[0]),y,'<')]))
    print(f"Part 2 - {best}")


                


    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
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

