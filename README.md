# two-brothers
take the input from the user
In the first case, there is only one cell, so Alice will play first and write a positive number.

In the second case, whatever value Alice writes in any of the cells, Bob can write the same value in his turn in the other cell.

To understand how the N values are computed, consider the following example:

Assume that the grid looks as follows after a game on a 2x3 grid

1 2 3
3 3 1
Then, in the end, two values will be computed:


1
⊕
2
⊕
3
=
0
, and

3
⊕
3
⊕
1
=
1
Since one of the values is 0, therefore in this game, Bob is the winner.

