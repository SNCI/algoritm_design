"""
       File : graph_to_file.py
     Author : Drew Verlee
       Date : 28.07.13.
      Email : drew.verlee@gmail.com
     GitHub : https://github.com/Midnightcoffee/
Description : from a graph create a file matching 
""" 

def graph_to_file(G, FILE_NAME="RWG.txt"):
    """creates random graph

    :G: networkx Graph object
    :creates: a graph file

    """
    graph_file = open(FILE_NAME, 'w')
    for node in G:
        graph_file.write(str(node))
        for neighbor in G[node]:
            graph_file.write(' ' +','.join(
                (str(neighbor),str(G[node][neighbor]['weight']))))
        graph_file.write('\n')
    graph_file.close()



if __name__ == '__main__':
    from build_graph import random_weighted_graph
    print('Graph size: '),
    size = input()
    G = random_weighted_graph(size)
    graph_to_file(G)
