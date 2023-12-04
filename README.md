# aoc2023

aiming for speed, my code is a mess. might rewrite later idk

```
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  4   00:03:20   188      0   00:14:51  1145      0
  3   01:08:04  7722      0   01:16:06  5682      0
  2   00:15:38  3080      0   00:18:33  2440      0
  1   00:02:03   219      0   00:08:05   173      0
```
1. Fast (but not fast enough)
2. Read too fast and missed the "mulpiple rounds per game, seperated by ';'" point, and then also typoed 'g'->'b'. Part 2 was <2 minutes once I got part 1 though
3. Didn't handle end of line case correctly (was only processing numbers after seeing a non-numeric symbol) and then overcomplicated things worrying about `+` and `-` signs. Once figured out, decently fast part 2
4. Fast (but not fast enough) part 1 , but then used array index instead of Game ID in initial part 2 implementation, which was wrong and delayed me a bit
