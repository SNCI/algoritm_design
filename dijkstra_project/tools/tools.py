"""
       File : test_build_graph.py
     Author : Drew Verlee
       Date : 28.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : tests for the tools used in Dijkstra algorithm
"""
from collections import defaultdict

def file_to_graph(file_name):
    """file is a undirected graph with first column a vertex and preceding columns
    its neighbors and there distances, neighbors are separated by commas

    example:
    >>> graph_file = StringIO()
    >>> graph_file.write('1 2,5 3,1\\n2 4,10\\n3 4,1'\\4, 3,1)
    >>> file_to_graph(graph_file)
    {1: {2: 5, 3:1},2: {4: 10},3: {4: 1},4: dict()}

    :file_name: A file object: vertex's and neighbors
    :returns: A dictionary: Graph

    """
    G = defaultdict(dict)
    with open(file_name) as f:
        for line in f:
            if line:
                line = line.split()
                v1, neighbors = line[0],line[1:]
                for neighbor in neighbors:
                    v2, weight = neighbor.split(',')
                    update_graph(G, v1, v2, weight)
    return G



def update_graph(G, v1, v2, weight=None): 
    v1, v2, weight = map(int, (v1, v2, weight))
    G[v1][v2] = weight

if __name__ == '__main__':
    import doctest
    doctest.testmod()

