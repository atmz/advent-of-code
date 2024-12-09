import sys; sys.dont_write_bytecode = True; from util import *

            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    line = lines[0]
    disk = []
    id = 0
    for i,c in enumerate(line):
        if i % 2 ==0:
            disk+=[id]*int(c)
            id+=1
        else:
            disk+=(['.']*int(c))
    print(disk)
    end_cursor = -1
    for i in range(1, len(disk)):
        if i>=(len(disk)+end_cursor):
            break
        while disk[end_cursor] == '.':
            end_cursor -= 1
        if disk[i] == '.':
            disk[i] = disk[end_cursor]
            disk[end_cursor] = '.'
    print("".join([str(d) for d in disk]))
    score = 0
    i=0
    while disk[i] != '.':
        score+=disk[i]*i
        i+=1
    print(score)
    #Part 2:
    line = lines[0]
    disk = []
    id = 0
    for i,c in enumerate(line):
        if i % 2 ==0:
            disk.append([id, int(c)])
            id+=1
        else:
            disk.append(['.', int(c)])
    original_disk = deepcopy(disk)
    for i in range(len(original_disk)-1, 0, -1):
        if original_disk[i][0] != '.':
            for j, spot in enumerate(disk):
                if spot[0] == '.' and spot[1] >= original_disk[i][1]:
                    disk.insert(j, original_disk[i])
                    spot[1] -= original_disk[i][1]
                    break
    flat_disk = []
    seen = set()
    for spot in disk:
        if spot[0] in seen:
            flat_disk+=('.'*spot[1]) 
        if spot[0] not in seen:
            flat_disk+=([spot[0]]*spot[1]) 
        if spot[0] != '.':
            seen.add(spot[0])
    print("".join([str(d) for d in flat_disk]))
    score=0
    for i,d in enumerate(flat_disk):
        if d!='.':
            score+=int(d)*i
    print(score)
    

                    
                   
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""2333133121414131402""",
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

