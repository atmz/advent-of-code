# aoc2024
Another year, another AOC. I still am using Python and aiming for speed over cleanliness, for the first week at least.

```
      --------Part 1---------   --------Part 2---------
Day       Time    Rank  Score       Time    Rank  Score
  6   01:32:07   12653      0   01:43:39    6510      0
  5   00:05:19     396      0   00:12:36     602      0
  4   01:09:24   11687      0   01:38:10   11396      0
  3   01:39:46   20002      0   01:41:57   15179      0
  2   01:36:14   18165      0   01:40:37   12007      0
  1       >24h  110383      0       >24h  104055      0
```
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