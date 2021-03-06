# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:36:49 2016

@author: johnzupan
"""

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph, labels=None, graph_layout='spring',
               node_size=1200, node_color='blue', node_alpha=0.3,
               node_text_size=10,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):
                   
    '''
    creates a network graph of artist nodes.
    graph (list of tuples): list of tuples of (artist1 name, artist2 name)
    
    Returns: a network graph
    '''

    # create networkx graph
    G=nx.Graph()

    # add edges
#    for edge in graph:
#        G.add_edge(edge[0], edge[1])

    G.add_edges_from(graph)
    # these are different layouts for the network you may try
    # spring seems to work best for what i want to show
    if graph_layout == 'shell':
        graph_pos=nx.shell_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.spring_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

#    if labels is None:
#        labels = range(len(graph))
#
#    edge_labels = dict(zip(graph, labels))
#    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
#                                 label_pos=edge_text_pos)

    # show graph
    plt.show()
