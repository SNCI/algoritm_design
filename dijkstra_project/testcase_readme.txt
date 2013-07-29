
Test Cases assignment 5 - dijkstra's algorithm

Please post only testcases
If your implementing in python you feel free to use my unittest and datafiles.


Additional I have created three scripts that might be of use to you:
They are located at my github repo here

File --------------------->use ------------------->     returns:
dijkstra.pyc      : $python Dijkstra start finish      shortest cost path
vizualizer.py     : $python file_name                  visualization of graph
weighted_graph_test_gen



Notes:
python2.7, may not work with version 3
$: From terminal

Dijkstra:
start: int: the starting vertex
finish: int: the vertex to which you want to find the shortest cost path
shortest cost path: int

test_generator:
file_name: str:
size: int: how many vertices

vizualizer
file_name: str:
visualization of graph: file: .png


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
Test Case large:





