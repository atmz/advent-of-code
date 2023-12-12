import sys; sys.dont_write_bytecode = True; from util import *


# Part 1 code, too slow for part 2
def is_possible(string, counts):
    section_index = 0
    current_count = 0
    in_section = False
    for c in string:
        if c == '?':
            return True
        if c == '#':
            current_count+=1
            if in_section:
                if  section_index>=len(counts) or current_count>counts[section_index] :
                    return False
            in_section=True
        if c == '.':
            if in_section:
                if  section_index>=len(counts) or current_count<counts[section_index]:
                    return False
                in_section=False
                section_index+=1
                current_count=0
    if in_section: # Case where we end with '#'
        if  section_index>=len(counts) or current_count<counts[section_index]:
            return False
        section_index+=1
        
    return section_index == len(counts)

def generate_possibilities(string, counts):
    if not is_possible(string, counts):
        return
    if '?' not in string:
        yield string
    else:
        for x in generate_possibilities(string.replace('?','.',1), counts):
            yield x
        for x in generate_possibilities(string.replace('?','#',1), counts):
            yield x

def count_possibilities(string, counts):
    i = 0
    for foo in generate_possibilities(string, counts):
        i+=1
    return i

# Part 2 code
cache = {}
def possibilities_with_remainder(string, counts, current_count=0, in_section=False):
    global cache
    section_index = 0
    if (string, ','.join([str(x) for x in counts[section_index:]]), current_count, in_section) in cache:
        return(cache[(string, ','.join([str(x) for x in counts[section_index:]]), current_count, in_section)])
    for i,c in enumerate(string):
        if c == '?':
            a_string = string[i:].replace('?','.',1)
            b_string =  string[i:].replace('?','#',1)
            a = possibilities_with_remainder(a_string, counts[section_index:], current_count, in_section)
            b = possibilities_with_remainder(b_string, counts[section_index:], current_count, in_section)
            cache[(a_string, ','.join([str(x) for x in counts[section_index:]]), current_count, in_section)] = a
            cache[(b_string, ','.join([str(x) for x in counts[section_index:]]), current_count, in_section)] = b
            return a+b
        if c == '#':
            current_count+=1
            if in_section:
                if section_index>=len(counts) or current_count>counts[section_index] :
                    return 0
            in_section=True
        if c == '.':
            if in_section:
                if section_index>=len(counts) or current_count<counts[section_index]:
                    return 0
                in_section=False
                section_index+=1
                current_count=0

    if in_section: # Case where we end with '#'
        if  section_index>=len(counts) or current_count<counts[section_index]:
            return 0
        section_index+=1
        
    if(section_index == len(counts)):
        return 1
    return 0

            


def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    grid = [list(x) for x in lines]


    
    score = 0
    for line in lines:
        string, counts = line.split()
        counts = [int(x) for x in counts.split(',')]
        score_line=count_possibilities(string, counts)
        score+=score_line
        # print(f"line: {line} possibilities: {score_line}")
    
        
    print(f"Part 1: {score}")


    score = 0
    for line in lines:
        string, counts = line.split()
        string = "?".join([string]*5)
        counts = ",".join([counts]*5)
        counts = [int(x) for x in counts.split(',')]
        score_line=0
        score_line=possibilities_with_remainder(string, counts)
        # print(cache)
        score+=score_line
        # print(f"line: {line} possibilities: {score_line}")
    
        
    print(f"Part 2: {score}")


    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
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

