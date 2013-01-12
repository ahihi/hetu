## Requirements

Python (tested on 2.6 and 2.7)

## Example

```
$ python hetu.py
Usage: hetu.py date1 date2
Dates must be in YYYY-MM-DD format and between years 1800 and 2999.
Date1 cannot be after date2.
$ python hetu.py 1990-01-30 1990-02-01
1990-01-30
  F: 0 -> 16, 1 -> 16, 2 -> 16, 3 -> 16, 4 -> 16, 5 -> 16,
     6 -> 16, 7 -> 16, 8 -> 16, 9 -> 16, A -> 16, B -> 16,
     C -> 16, D -> 17, E -> 16, F -> 17, H -> 16, J -> 17,
     K -> 16, L -> 17, M -> 16, N -> 16, P -> 16, R -> 16,
     S -> 16, T -> 16, U -> 16, V -> 16, W -> 16, X -> 16,
     Y -> 16.
  M: 0 -> 16, 1 -> 16, 2 -> 16, 3 -> 16, 4 -> 16, 5 -> 16,
     6 -> 16, 7 -> 16, 8 -> 16, 9 -> 16, A -> 16, B -> 16,
     C -> 16, D -> 16, E -> 17, F -> 16, H -> 17, J -> 16,
     K -> 17, L -> 16, M -> 16, N -> 16, P -> 16, R -> 16,
     S -> 16, T -> 16, U -> 16, V -> 16, W -> 16, X -> 16,
     Y -> 16.

1990-01-31
  F: 0 -> 16, 1 -> 16, 2 -> 17, 3 -> 16, 4 -> 17, 5 -> 16,
     6 -> 17, 7 -> 16, 8 -> 17, 9 -> 16, A -> 16, B -> 16,
     C -> 16, D -> 16, E -> 16, F -> 16, H -> 16, J -> 16,
     K -> 16, L -> 16, M -> 16, N -> 16, P -> 16, R -> 16,
     S -> 16, T -> 16, U -> 16, V -> 16, W -> 16, X -> 16,
     Y -> 16.
  M: 0 -> 16, 1 -> 16, 2 -> 16, 3 -> 17, 4 -> 16, 5 -> 17,
     6 -> 16, 7 -> 17, 8 -> 16, 9 -> 16, A -> 16, B -> 16,
     C -> 16, D -> 16, E -> 16, F -> 16, H -> 16, J -> 16,
     K -> 16, L -> 16, M -> 16, N -> 16, P -> 16, R -> 16,
     S -> 16, T -> 16, U -> 16, V -> 16, W -> 16, X -> 16,
     Y -> 16.

1990-02-01
  F: 0 -> 16, 1 -> 16, 2 -> 16, 3 -> 16, 4 -> 16, 5 -> 16,
     6 -> 16, 7 -> 16, 8 -> 16, 9 -> 16, A -> 16, B -> 16,
     C -> 16, D -> 16, E -> 16, F -> 16, H -> 17, J -> 16,
     K -> 17, L -> 16, M -> 17, N -> 16, P -> 17, R -> 16,
     S -> 16, T -> 16, U -> 16, V -> 16, W -> 16, X -> 16,
     Y -> 16.
  M: 0 -> 16, 1 -> 16, 2 -> 16, 3 -> 16, 4 -> 16, 5 -> 16,
     6 -> 16, 7 -> 16, 8 -> 16, 9 -> 16, A -> 16, B -> 16,
     C -> 16, D -> 16, E -> 16, F -> 16, H -> 16, J -> 17,
     K -> 16, L -> 17, M -> 16, N -> 17, P -> 16, R -> 16,
     S -> 16, T -> 16, U -> 16, V -> 16, W -> 16, X -> 16,
     Y -> 16.

Overall frequencies
  F: 0 -> 3.20%, 1 -> 3.20%, 2 -> 3.27%, 3 -> 3.20%, 4 -> 3.27%, 5 -> 3.20%,
     6 -> 3.27%, 7 -> 3.20%, 8 -> 3.27%, 9 -> 3.20%, A -> 3.20%, B -> 3.20%,
     C -> 3.20%, D -> 3.27%, E -> 3.20%, F -> 3.27%, H -> 3.27%, J -> 3.27%,
     K -> 3.27%, L -> 3.27%, M -> 3.27%, N -> 3.20%, P -> 3.27%, R -> 3.20%,
     S -> 3.20%, T -> 3.20%, U -> 3.20%, V -> 3.20%, W -> 3.20%, X -> 3.20%,
     Y -> 3.20%.
  M: 0 -> 3.21%, 1 -> 3.21%, 2 -> 3.21%, 3 -> 3.27%, 4 -> 3.21%, 5 -> 3.27%,
     6 -> 3.21%, 7 -> 3.27%, 8 -> 3.21%, 9 -> 3.21%, A -> 3.21%, B -> 3.21%,
     C -> 3.21%, D -> 3.21%, E -> 3.27%, F -> 3.21%, H -> 3.27%, J -> 3.27%,
     K -> 3.27%, L -> 3.27%, M -> 3.21%, N -> 3.27%, P -> 3.21%, R -> 3.21%,
     S -> 3.21%, T -> 3.21%, U -> 3.21%, V -> 3.21%, W -> 3.21%, X -> 3.21%,
     Y -> 3.21%.
```