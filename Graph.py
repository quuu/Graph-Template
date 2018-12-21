'''
Graph class
Directed
'''

from Edge import *

class Graph:

    '''
    Constructor of Graph object

    @effects __nodes : initialized with empty dictionary
    @modifies __nodes
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

        # currently converts the node values to strings
        start = str(start)
        end = str(end)
        if(start not in self.__nodes):
            self.__nodes[start] = []
        self.__nodes[start].append(Edge(value,end))
        self.checkRep()

    '''
    Gets neighbors of Node(node)

    @param node : node value to get neighbors of
    @returns list  copy of neighbors of Node(node)
    '''
    def getNeighbors(self, node):
        return list(self.__nodes[node])


    '''
    Lists all the nodes in the graph

    @returns list copy of keys in nodes
    '''
    def listNodes(self):
        return list(self.__nodes.keys())

    '''
    TODO: print representation
    '''
    def __str__(self):
        return ""

    '''
    TODO: shortest path from one node to another
    given numerical edge labels

    @param start : Node(start) to start at
    @param end : Node(end) to end at
    @return String of path to get from start to end, or that no path is found
    '''
    def shortestPath(self, start, end):
        return ""

    '''
    TODO: check representation to make sure types are consistent
    ex: all edge weights are String and all nodes are Int

    Only need to checkRep when adding an edge? Otherwise immutable?
    - All Edge labels are of same type
    - All Node values are of the same type
    - No reflexive edges
    '''
    def checkRep(self):
        print("checking rep")



'''
Quick tests

'''
g = Graph()
g.addEdge('a', 10, 'b')
g.addEdge('e', 10, 'c')
g.addEdge('f', 10, 'd')
l = g.listNodes()
print(l)
