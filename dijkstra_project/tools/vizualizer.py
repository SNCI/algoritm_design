#!/usr/bin/env python
"""
       File : visualizer.py
     Author : Drew Verlee
       Date : 28.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : code reproduced from  Aric Haberg's (hagberg@lanl.gov)
An example using Graph as a weighted network.
from here https://groups.google.com/forum/#!topic/networkx-discuss/hw3OVBF8orc
"""

import pylab
import networkx as nx


def visualize_weighted_graph(file_name):
    """@todo: Given a file with file that is a graph with first
    column a vertex and preceding columns
    its neighbors and there distances, neighbors are separated by commas

    :a_file: name of the file
    :creates: graph visualization of the Graph and saves it as a file_name.png

    """
    G = nx.Graph()
    with open(file_name) as f:
        for line in f:
            if line:
                line = line.split()
                v1, neighbors = line[0],line[1:]
                for neighbor in neighbors:
                    v2, weight = neighbor.split(',')
                    G.add_edge(v1, v2, weight=int(weight))

    pos=nx.spring_layout(G)
    pylab.figure(2)
    nx.draw(G,pos)
    edge_labels=dict([((u,v,),d['weight'])
                for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    pylab.savefig(file_name.replace('txt','png'))



if __name__ == '__main__':
    import sys
    file_name = sys.argv[1]

    visualize_weighted_graph(file_name)
