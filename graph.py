'''
Graph class

'''

from node import *
from Edge import *
class Graph:

    '''
    Constructor of Graph object
    '''
    def __init__(self):
        # dictionary with key -> value : node -> adjacency list
        self.__nodes = {}


    '''
    Add an edge from node value a to node value b
    values a and b get converted to string values automatically

    @param a : node value edge starts from
    @param b : node value edge points to
    @param value : edge weight between Node(a) and Node(b)
    '''

    def addEdge(self, start, value, end):
        start = str(start)
        end = str(end)
        if(start not in self.__nodes):
            self.__nodes[start] = []
        self.__nodes[start].append(Edge(value,end))

    '''
    Gets neighbors of Node(node)

    @param node : node value to get neighbors of
    '''
    def getNeighbors(self, node):
        return self.__nodes[node]

    '''
    TODO: print representation
    '''
    def __str__(self):
        return ""

'''
Quick tests

'''
"""
g = Graph()
g.addEdge('a', 10, 'b')
g.addEdge('a', 10, 'c')
g.addEdge('a', 10, 'd')
print(g.getNeighbors('a'))
"""
