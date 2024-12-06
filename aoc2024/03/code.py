import sys; sys.dont_write_bytecode = True; from util import *


            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    matches = re.findall(r"mul\([0-9]?[0-9]?[0-9],[0-9]?[0-9]?[0-9]\)|do\(\)|don\'t\(\)", inp)
    part_1 = 0
    part_2 = 0
    do = True
    print(matches)
    for m in matches:
        if m == "do()":
            do = True
        elif m == "don't()":
            do = False
        else:
            m = m[4:-1]
            a,b = m.split(",")
            part_1 += int(a) * int(b)
            if do:
                part_2 += int(a) * int(b)
    print(part_1, part_2)





    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""",
    r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)

