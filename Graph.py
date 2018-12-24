'''
Graph class
Directed
'''

from Edge import *

class DirectedGraph(object):

    '''
    Constructor of Graph object

    @effects __nodes : initialized with empty dictionary
    @modifies __nodes
    '''
    def __init__(self, maintain=True):
        # dictionary with key -> value : node -> adjacency list
        self.__nodes = {}
        self.maintainRep = maintain



    '''
    Add an edge from node value a to node value b
    values a and b get converted to string values automatically

    TODO: allow node values not only be strings

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
        if (end not in self.__nodes):
            self.__nodes[end] = []
        self.__nodes[start].append(Edge(value, end))
        # self.__nodes[end].append(Edge(value,start))
        if(self.maintainRep is True):
            self.checkRep()

    '''
    Gets neighbors of Node(node)

    @param node : node value to get neighbors of
    @returns list  copy of neighbors of Node(node)
    '''
    def getNeighbors(self, node):
        if (node not in self.__nodes):
            raise Exception('Node value not found')
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

    @requires __nodes to have edge labels of ints or doubles

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
    - All Edge labels are of same type x
    - All Node values are of the same type
    - No reflexive edges x


    @throws Exception if any of the representation invariants are broken
    '''
    def checkRep(self):
        # checking for reflexive edge
        try:
            for key, value in self.__nodes.items():
                for e in value:
                    if(key is e.getNext()):
                        raise Exception('There is a reflexive edge in the graph')
        except Exception as err:
            print(err.args)
            raise

        # checking for same edge types
        try:
            t=None
            for key, value in self.__nodes.items():
                for e in value:
                    if(t is None):
                        t = type(e.getLabel())
                        continue
                    if(not type(e.getLabel()) is t):
                        raise Exception('Edge value types not the same')
        except Exception as err:
            print(err.args)
            raise

        # checking for same node types
        try:
            t=None
            for key, value in self.__nodes.items():
                if(t is None):
                    t = type(key)
                    continue
                if(not type(key) is t):
                    raise Exception('Node value types not the same')
        except Exception as err:
            print(err.args)
            raise




'''
Quick tests

'''

g = DirectedGraph(False)
g.addEdge('a', 10, 'b')
g.addEdge('e', 10, 'c')
g.addEdge('f', 10, 'b')
l = g.listNodes()
print(l)
# l = g.getNeighbors('e')
# print(l)
# l = g.getNeighbors('m')
# print(l)

