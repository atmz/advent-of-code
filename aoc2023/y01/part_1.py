import sys; sys.dont_write_bytecode = True; from util import *

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    ratings = defaultdict(list)
    score=0
    score_2 = 0
    for line in lines:
        if line:
            a,b = line.split(",")
            a = int(a)
            b= int(b)
            ratings[a].append( float(b))
    for biz in ratings.keys():
        ratings[biz] = sorted(ratings[biz])
        if len(ratings[biz]) % 2 == 1:
            m = ratings[biz][len(ratings[biz])//2]
        else:
            m = (ratings[biz][len(ratings[biz])//2]+ratings[biz][len(ratings[biz])//2-1])/2
       
        ratings[biz] = float(sum(ratings[biz]))/len(ratings[biz])
        new_rating = round(ratings[biz]+m)/2
        ratings[biz] = round(ratings[biz]*2)/2
        if ratings[biz] == 4.5:
            score+=1
        if new_rating == 4.5:
            score_2+=1
        
                
            
    
    print(score, score_2)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""123, 4
123, 5
234, 5
234, 5
234, 1
123, 5
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

