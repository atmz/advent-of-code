import sys; sys.dont_write_bytecode = True; from util import *
from sympy.abc import a,b,c

def combo_operator(operand, registers):
    if operand<4:
        return operand
    elif operand == 4:
        return registers[a]
    elif operand == 5:
        return registers[b]
    elif operand == 6:
        return registers[c]
    else:
        assert False

def run_instruction(inst, operand, registers, pc):
    out = None
    if inst == 0: #adv
        registers[a] = registers[a]//(2**combo_operator(operand, registers))
    if inst == 1: # bxl
        registers[b] = registers[b] ^ operand
    if inst == 2: # bst
        registers[b] = combo_operator(operand, registers) % 8
    if inst == 3: # jnz
        if registers[a] != 0:
            pc = operand
            return pc, out
    if inst == 4: # bxc
        registers[b] = registers[b] ^ registers[c]
    if inst == 5: # bxc
        out = combo_operator(operand, registers) % 8
    if inst == 6: #bdv
        registers[b] = registers[a]//(2**combo_operator(operand, registers))
    if inst == 7: #cdv
        registers[c] = registers[a]//(2**combo_operator(operand, registers))

    pc+=2
    return pc, out

def guess_generator():
    # Magic numbers determined by observation
    base=2**29
    increment=2**29
    index=0
    mods = [1359348,5553652,5684724,9747956]
    while True:
        yield base+mods[index]
        index+=1
        if index>=len(mods):
            index=0
            base+=increment


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    registers = {
        a:int(lines[0].split(':')[1]),
        b:int(lines[1].split(':')[1]),
        c:int(lines[2].split(':')[1]),
    }
    pc = 0
    program_output = []
    program = [int(i) for i in lines[4].split(':')[1].split(',')]
    try:
        while True:
            pc, out = run_instruction(program[pc], program[pc+1], registers, pc)
            if out is not None:
                program_output.append(out)
    except IndexError:
        print("Part 1:", ",".join([str(i) for i in program_output]))
    
    generator = guess_generator()
    while program_output!=program:
        i = generator.__next__()
        pc=0
        program_output=[]
        registers = {
            a:int(i),
            b:int(lines[1].split(':')[1]),
            c:int(lines[2].split(':')[1]),
        }
        try:
            while True:
                pc, out = run_instruction(program[pc], program[pc+1], registers, pc)
                # print(program[pc],pc, out, registers)
                if out is not None:
                    program_output.append(out)
                    if program_output != program[:len(program_output)]:
                        break
        except IndexError:
            pass
    print("Part 2:", i)
    
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
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

