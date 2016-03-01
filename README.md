Question: Implement Outer join in python with duplicate keys using hash efficiency. The two input tables are stored as csv files.

Input:

math.csv
    id, math
    1,A
    2,B
    3,C
    3,F
    
verb.csv
    id,verb
    2,A
    3,C
    3,E
    4,B

Output:

[['1', 'A', None],
 ['3', 'C', 'C'],
 ['3', 'C', 'E'],
 ['3', 'F', 'C'],
 ['3', 'F', 'E'],
 ['2', 'B', 'A'],
 ['4', None, 'B']]
