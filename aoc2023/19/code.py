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
    
    instructions = {}
    parts = []

    i = 0
    while len(lines[i])>0:
        label, rest = lines[i].split("{")
        rules = []
        for workflow_string in rest.strip("}").split(","):
            if ':' in workflow_string:
                condition, destination = workflow_string.split(':')
                rules.append( (condition,destination) )
            else:
                rules.append( (workflow_string,) )
        instructions[label]=rules
        i+=1

    while len(lines[i])==0:
        i+=1
    while len(lines)>i and len(lines[i])>0:
        value_strings = lines[i].strip("{}").split(",")
        for value_string in value_strings:
            var, value = value_string.split('=')
            if var == 'x':
                x = int(value)
            if var == 'm':
                m = int(value)
            if var == 'a':
                a = int(value)
            if var == 's':
                s = int(value)
        parts.append(
            {
                'x':x,
                'a':a,
                'm':m,
                's':s,
            }
        )
        i+=1

    def process(instructions, part):
        x = part['x']
        a = part['a']
        m = part['m']
        s = part['s']
        result = None
        for instr in instructions:
            if len(instr) == 1:
                result = instr[0]
                break 
            condition, dest = instr
            if( eval(condition) ):
                result = dest
                break
        return result
        



    score = 0
    for part in parts:
        current = 'in'
        while current not in ['A', 'R']:
            current = process(instructions[current], part)
        if current == 'A':
            score += sum(part.values())
    
    print(f"Part 1: {score}")


    score=0

    states = [{
        'x' : [1,4001],
        'm' : [1,4001],
        'a' : [1,4001],
        's' : [1,4001],
        'i' : "in",
        'pre' : None
    }]
    print(instructions)

    def permutations(state):
        if state['pre'] == 'A':
            print(f"!!!!:")
            return 0
        if (state['x'][1]<state['x'][0]) or (state['m'][1]<state['m'][0]) or (state['a'][1]<state['a'][0]) or (state['s'][1]<state['s'][0]):
            print(f"!!!!:")
            return 0
        result = (state['x'][1]-state['x'][0])*(state['m'][1]-state['m'][0])*(state['a'][1]-state['a'][0])*(state['s'][1]-state['s'][0])
        print(f"result:{result}")
        return result
    while states:
        state = states.pop()

        if state['i'] == 'R':
            continue
        if state['i'] == 'A':
            print(state)
            score+=permutations(state)
            continue
        instruction = instructions[state['i']]
        for instr in instruction:
            if len(instr) == 1:
                state['pre'] = state['i'] 
                state['i'] = instr[0]
                break
            else:
                condition, dest = instr
                if '<' in condition:
                    flag, value = condition.split('<')
                    value = int(value)
                    current = state[flag]
                    if current[1]>value and current[0]<value:
                        # we need to split
                        new = deepcopy(state)
                        current[0] = value 

                        new[flag][1]=value
                        new['pre'] = new['i'] 
                        new['i'] = dest
                        states.append(new)

                if '>' in condition:
                    flag, value = condition.split('>')
                    value = int(value)
                    current = state[flag]
                    # print(f"current:{current} value{value}")
                    if current[1]>value and current[0]<value:
                        # we need to split
                        new = deepcopy(state)
                        current[1]=value+1

                        new[flag][0]=value+1
                        new['pre'] = new['i'] 
                        new['i'] = dest
                        states.append(new)

        states.append(state)
        # print(states)
        

    


    

        
        

    print(f"Part 2: {score}")






                


    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}


{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
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

