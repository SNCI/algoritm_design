Test Cases assignment 5 - dijkstra's algorithm

Please post only testcases

Additional I have created three scripts that might be of use to you,
they along, with my unitests and datafiles are located at my github repo here.

File --------------------->use ------------------->         returns:
dijkstra.pyc      : $python Dijkstra start finish      shortest cost path
vizualizer.py     : $python file_name                 visualization of graph
test_generator    : $python test_generator.py         graphs/result and graphs


Notes:
python2.7, may not work with version 3
$: From terminal

Dijkstra:
start: int: the starting vertex
finish: int: the vertex to which you want to find the shortest cost path
shortest cost path: int

vizualizer
file_name: str: a file of the same specifications as our assignment file
visualization of graph: file: .png

test_generator:
when you run python test_generator it will let you choose the number of graphs
and the size you wish to create. Then it "magical" will create folder "graphs"
that will contain result.txt. result.txt will tell you which graph in they
graph folder failed.

Example: $python test_generator
how many tests? 3
what size graph? 10

   graphs/ <- folder created
      graph0.png
      graph0.txt
      graph1.png
      graph1.txt
      graph2.png
      graph2.txt
      results.txt <- results -> 

if you open results..
Graph0 failed to find lowest cost 48 with path [9, 4, 7]
Graph1 failed to find lowest cost 37 with path [9, 7]
Graph2 failed to find lowest cost 29 with path [8, 6, 1, 3, 0]

then take a look at graph0.png for the visual aid

IF your NOT using python this can only be used to generate test files 
If you are using python you can modify test_generator:

    from dijkstra import dijkstra #FIXME change me to use your algorithm

to test your algorithm against
                    TEST CASES
****************************************************************

Test Case small:

input:
    1 2,5 3,1
    2 4,10 1,5
    3 4,1 1,1
    4 2,10 3,1

    start =  1
    finish = 4

expected cost: 2
****************************************************************
Test Case medium:
input:
    1   2,2     4,1
    2   4,3     5,10
    3   1,4     6,5
    4   3,2     5,2     6,8     7,4
    5   7,6
    7   6,1

    start = 1
    finish = 7

expected cost: 5
****************************************************************
0 1,28 2,4 3,53 4,95 5,59 7,48 8,84 10,27 11,7 12,91 13,96
1 0,28 2,79 5,30 7,59 8,62 9,20 11,15 12,16 13,96
2 0,4 1,79 3,80 5,19 6,74 8,59 10,80 11,81 12,65 13,7 14,13
3 0,53 2,80 4,87 5,42 6,70 7,8 12,44 13,92
4 0,95 3,87 5,86 6,46 7,44 9,12 10,39 12,14 13,95 14,19
5 0,59 1,30 2,19 3,42 4,86 6,12 7,0 8,72 10,92 11,54 12,0 13,68 14,22
6 2,74 3,70 4,46 5,12 7,86 9,76 10,68 11,32 12,62 13,34
7 0,48 1,59 3,8 4,44 5,0 6,86 8,38 9,34 10,12 11,55 12,25 14,9
8 0,84 1,62 2,59 5,72 7,38 10,66 11,31 12,95
9 1,20 4,12 6,76 7,34 10,63 11,37 12,93 13,79
10 0,27 2,80 4,39 5,92 6,68 7,12 8,66 9,63 12,45 14,78
11 0,7 1,15 2,81 5,54 6,32 7,55 8,31 9,37 12,75 13,87
12 0,91 1,16 2,65 3,44 4,14 5,0 6,62 7,25 8,95 9,93 10,45 11,75 13,46 14,63
13 0,96 1,96 2,7 3,92 4,95 5,68 6,34 9,79 11,87 12,46
14 2,13 4,19 5,22 7,9 10,78 12,63





