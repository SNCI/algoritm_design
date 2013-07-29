
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





