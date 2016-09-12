# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:37:06 2016

@author: johnzupan
"""
import extractData
import createNetworkGraph as c
import wikiMain as w
reload(extractData)
reload(c)
reload(w)


def createFullWikiWeb(startingURL, startingArtist, numOfLoops):
    '''
    This function creates the network graph of related artists using a 
    breadth first search of wikipedia.
    startingURL (str): the wikipedia link of the staring artist
    startingArtist (str): the name of the starting artist
    numOfLoops (int): how many nodes the function should expand
    
    Returns: a network graph of an artist and their associated acts
    '''
    
    #collect the node and edges data from wikipedia
    rawGraph = w.main(startingURL, startingArtist, numOfLoops)
    
    #remove the wiki links to clean up the nodes    
    finalGraph = []
    for i, j, t, q  in rawGraph:
        newT = (j, q)
        finalGraph.append(newT)
        
    #draw the graph
    return c.draw_graph(finalGraph)
    
    