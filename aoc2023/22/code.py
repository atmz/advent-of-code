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


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    blocks = []
    settled_coords = {}
    settled_blocks = set()
    depends_on = {}
    lines = [row for row in inp.splitlines()]
    print(lines)
    for i, line in enumerate(lines):
        a,b = line.split('~')
        a = tuple([int(x) for x in a.split(',')])
        b = tuple([int(x) for x in b.split(',')])
        if a[0] != b[0]:
            assert a[1] == b[1]
            assert a[2] == b[2]
        if a[1] != b[1]:
            assert a[0] == b[0]
            assert a[2] == b[2]
        if a[2] != b[2]:
            assert a[1] == b[1]
            assert a[0] == b[0]
        
        blocks.append((a,b, i))
        depends_on[i] = set()
    blocks.sort(key=lambda x: min(x[0][2], x[1][2]))

    def is_vert(block):
        return block[0][2] != block[1][2]


    def is_settled(block):
        a = block[0]
        b = block[1]
        if a[2] == 1 or b[2] == 1:
            return True
        for coord in get_coords_one_below(block):
            if coord in settled_coords:
                return True
        return False
    
    def settled_on(block):
        result = set()
        a = block[0]
        b = block[1]
        if a[2] == 1 or b[2] == 1:
            return set()
        for coord in get_coords_one_below(block):
            if coord in settled_coords:
                result.add(settled_coords[coord])
                depends_on[block[2]].add(settled_coords[coord])
        return result
    
    def drop_block(block):
        return ((block[0][0], block[0][1], block[0][2]-1), (block[1][0], block[1][1], block[1][2]-1), block[2])

    while blocks:
        print("interation")
        next_blocks = []
        for block in blocks:
            if is_settled(block):
                print(block)
                for x in range(block[0][0], block[1][0]+1):
                    for y in range(block[0][1], block[1][1]+1):
                        for z in range(block[0][2], block[1][2]+1):
                            if (x,y,z) in settled_coords:
                                print("OVERLAP?", block, settled_coords[(x,y,z)])
                                assert False
                            settled_coords[(x,y,z)] = block[2]
                settled_blocks.add(block)
            else:
                next_blocks.append(drop_block(block))
        blocks = next_blocks
    print(settled_blocks)
    print(settled_coords)
    
    can_delete = set([x[2] for x in settled_blocks])
    
    for block in settled_blocks:
        if len(settled_on(block)) == 1 and list(settled_on(block))[0] in can_delete:
            can_delete.remove(list(settled_on(block))[0])
        
            
    print("Part 1", len(can_delete))
    print(depends_on)
    score = 0
    for block in settled_blocks:
        subscore = 0
        to_delete = [block[2]]
        depends = deepcopy(depends_on)
        while len(to_delete):
            next_to_delete = to_delete.pop()
            for i in depends.keys():
                if next_to_delete in depends[i]:
                    depends[i].remove(next_to_delete)
                    if not depends[i]:
                        to_delete.append(i)
                        subscore += 1
        score += subscore
        print(block, score)
    print("Part 2", score)
    

        

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""",
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

