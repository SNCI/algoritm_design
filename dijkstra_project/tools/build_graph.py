"""
       File : build_graph.py
     Author : Drew Verlee
       Date : 28.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : creates a random weighted graph
"""


import networkx as nx
from math import ceil
from random import randrange as rr

def random_weighted_graph(size):
    """Creates random graph

    :size: int: number of nodes in graph
    :returns: nx.Graph object

    """
    nodes = size
    edges = nodes* (nodes/2) # densely connected
    MAX_WEIGHT = 100
    G = nx.dense_gnm_random_graph(n=nodes, m=edges)
    # give our graph some random weights
    for edge in G.edges(): G.add_edge(*edge, weight = rr(MAX_WEIGHT))
    assert nx.is_connected(G) == True # make sure its connected
    return G

if __name__ == '__main__':
    print('Graph size: '),
    size = input()
    G = random_weighted_graph(size)
    print(G)



