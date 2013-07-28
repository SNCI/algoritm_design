"""
       File : test_generator.py
     Author : Drew Verlee
       Date : 28.07.13.
     GitHub : https://github.com/Midnightcoffee/
Description : to create a graph file
"""

from collections import defaultdict as dd
from random import randrange as rr
def graph_file_gen(file_name, size):
    """creates a file, that contains the contents of a graph with
    the first column as a node and the subsequent columns as neighbor,weight
    example:

    1 2,3
    2 1,3

    :file_name: file object:
    :size: how many verticies, recommended over 50
    :creates: a file named file_name in current directory

    """
    G = dd(dict)
    with open(file_name, 'w') as f:
        for node in xrange(1, size):
            f.write(str(node))
            high = rr(size//10, size)/2
            # make every node pass through 1
            if node != 1: f.write(' ' + str(1) + ',' + str(1))
            update_graph(G, node, 1, 1)
            for i in xrange(high):
                x = rr(size)
                if x != node:
                    if x in G and node in G[x]:
                        weight = G[x][node]
                    else:
                        weight = rr(1,100)
                    update_graph(G, node, x, weight)
                    f.write(' ' + str(x) + ',' + str(weight))
            f.write('\n')

def update_graph(G, v1, v2, weight):
    G[v1][v2] = weight
    G[v2][v1] = weight

if __name__ == '__main__':
    import sys
    file_name, size = sys.argv[1:]
    graph_file_gen('.'.join((file_name,'txt')), int(size))


