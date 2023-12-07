# aoc2023

aiming for speed, my code is a mess. might rewrite later idk

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  7   00:21:09   1094      0   01:42:22   7213      0
  6   01:40:00  15657      0   01:40:55  14673      0
  5   00:19:58   1328      0   02:20:35   5145      0
  4   00:03:20    188      0   00:14:51   1145      0
  3   01:08:04   7722      0   01:16:06   5682      0
  2   00:15:38   3080      0   00:18:33   2440      0
  1   00:02:03    219      0   00:08:05    173      0
```
1. Fast (but not fast enough)
2. Read too fast and missed the "mulpiple rounds per game, seperated by ';'" point, and then also typoed 'g'->'b'. Part 2 was <2 minutes once I got part 1 though
3. Didn't handle end of line case correctly (was only processing numbers after seeing a non-numeric symbol) and then overcomplicated things worrying about `+` and `-` signs. Once figured out, decently fast part 2
4. Fast (but not fast enough) part 1 , but then used array index instead of Game ID in initial part 2 implementation, which was wrong and delayed me a bit
5. Tedious problem. Incredible innefficent part 1, so did a complete rewrite for part 2
6. Late start due to life - actual time taken around 3:30 for part 1, 4:30 for part 2 (but I got some thinking time). Classic easy puzzle, part 1 solution Just Worked for part 2
7. TIL that Python3 deprecates `cmp` and also that `key` is faster and cleaner. Part 1 was straightforward but I was a bit slow. I tried to be too smart and count unique cards to figure out rankings quickly, but that got too messy for part 2, so I stopped, had breakfast, and rewrote it a little more cleanlygit 
