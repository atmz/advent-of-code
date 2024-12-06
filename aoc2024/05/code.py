import sys; sys.dont_write_bytecode = True; from util import *


            

def fix(pages, rules):
        print("Pages", pages)
        fail=True
        while fail:
            seen = {}
            fail = False
            for i, page in enumerate(pages):
                if fail:
                    break
                page = page.strip()
                for rule in rules:
                    seen[page]=i
                    if rule[0] == page and rule[1] in seen:
                        fail = True
                        pages[i] = rule[1]
                        pages[seen[rule[1]]] = rule[0]
                        break
        print("Fixed", pages)
        return pages
                        
                

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    rules = set()
    score = 0
    score2 = 0
    for line in lines:
        if '|' in line:
            a, b = line.split('|')
            a = a.strip()
            b = b.strip()
            rules.add((a,b))
        else:
            pages = line.split(',')
            seen = set()
            fail = False
            for page in pages:
                page = page.strip()
                for rule in rules:
                    if rule[0] == page and rule[1] in seen:
                        fail = True
                    seen.add(page)
            if not fail and len(seen)>1:
                print(pages)
                middle_page = pages[len(pages)//2]
                score += int(middle_page)
            elif fail:
                pages=fix(pages, rules)
                middle_page = pages[len(pages)//2]
                score2 += int(middle_page)
    

    print(score)
    print(score2)
    
    
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
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

