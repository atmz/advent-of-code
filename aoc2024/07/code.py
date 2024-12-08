import sys; sys.dont_write_bytecode = True; from util import *

            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    score = 0
    def  is_possible(value, parts):
        if len(parts) == 1:
            return value == parts[0]
        if value % parts[-1] == 0 and is_possible(value // parts[-1], parts[:-1]):
            return True
        # Comment out for part 1
        if str(value).endswith(str(parts[-1])) and len(str(value)) > len(str(parts[-1])):
            if is_possible(int(str(value)[:-len(str(parts[-1]))]), parts[:-1]):
                return True
        if value - parts[-1] >= 0 and is_possible(value - parts[-1], parts[:-1]):
            return True
        return False
    for line in lines:
        value, b = line.split(':')
        value = int(value)
        parts = [int(x) for x in b.split()]
        if is_possible(value, parts):
            score += value


    print(score)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""",
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

