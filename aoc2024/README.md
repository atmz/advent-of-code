# aoc2024
Another year, another AOC. I still am using Python and aiming for speed over cleanliness, for the first week at least.

```
      --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
 14   03:11:09   10535      0   03:25:19    7955      0
 13   00:49:02    5189      0   07:56:04   15517      0
 12   01:31:13    8192      0   02:53:13    5722      0
 11   00:04:29     469      0   01:38:18    6888      0
 10   00:53:16    7328      0   00:54:11    6552      0
  9   00:35:35    4519      0   01:38:44    4813      0
  8   01:21:12    8540      0   01:26:29    7487      0
  7   01:05:25    8674      0   01:13:01    7612      0
  6   01:32:07   12653      0   01:43:39    6510      0
  5   00:05:19     396      0   00:12:36     602      0
  4   01:09:24   11687      0   01:38:10   11396      0
  3   01:39:46   20002      0   01:41:57   15179      0
  2   01:36:14   18165      0   01:40:37   12007      0
  1       >24h  110383      0       >24h  104055      0
```
14. Part 1 was pretty easy, you can figure out where anything will be in n steps in O(1). Unfortunately, I had an off-by-one error that worked on the example, so I wasted a ton of time here. Part 2 was a surprise, but my christmas-tree-detecting logic worked fine enough, and edned up spending <15 minutes on part 2
13. Naive solution for part 1 worked fine, part 2 I tried various bad optimzations before giving up and solving the equation with sympy. In retrospect could have done this geometrically I think?
12. Getting into the harder content! Re-used skeleton of part 2, started at 8ish so actually did part 1 pretty quickly. Perimiter calculations actually can be done neatly in the same recursive algorithm. In Part 2, it's trickier -- I tried to be clever but we need to do the full traversal before we can correctly count sides. So, ended up saving all the edges, then sorting (important!) and counting only edges that haven't had a neighbor seen yet
11. Sub 5 minute part 1, part 2 needed a more efficient implementation and I needed to help with kids. Did part 2 using a defaultdict(int) to count rocks, and that ran fast enough
10. Pretty simple graph traversal, did it recursively and part 2 is very similar to part 1 (I actually implemented part 2 by accident first)
9. Easy Monday puzzle? Part 2 bneeded a rewrite from my very simple Part 1, but both worked pretty easily. Started at 7:11, did aprt 1, took kids to school, then did part 2
8. Started at 8:16ish, but a nice puzzle and got to a pretty quick solution that worked first time
7. Started at 7:43, fun problem -- fairly naive solution worked, but only after replacing `set(itertools.permutations(` with `itertools.product([<>], repeat=X)` for the operator permutation logic. Went back later and figured out a massive optimization - do things end-first, and then because everything is integer your options become way more limited
6. Started around 8:30, was pretty quick and fairly nice solution -- part 1 is straightforward, part 2 is brute-force with some optimizations 
(e.g. only obstacles on the path can do anything, so that reduces our search space a LOT)
5. First one I managed to start as soon as it dropped, and a fun quick problem. 
Part 1: track seen pages, and if you get the first page in a rule and have seen the second already, fail
Part 2: take every list that fails, and swap the failed pair. Repeat until it no longer fails. This felt naive but worked.
4. Part 1 - regex again, some tricky logic to get diagonals into strings which I messed up a few times. Part 2 I misread and thought we were looking for 
'+'s as well as 'X's which confused/slowed me down. I like my solution (find all A's and then check their surroundings)
3. started around 8am again, regex basically doing it all here
2. Forgot about AOC until 8:30 am or so, did it in ~12 minutes once I remembered
1. Forgot about AOC completely, timed myself at part 1 - 2:05, part 2 - 4:00 once I got around to it