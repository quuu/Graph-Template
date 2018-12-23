

from Graph import *
import heapq
'''
Sample code for how to expand functionality of Graph class
from outside the class

Implementation of Dijkstra's algorithm on a formed Directed Graph
'''
def shortestPath(graph, start, end):
    q = []
    visited = []
    heapq.heappush(q,start)
    return q


if __name__ == '__main__':
    g = DirectedGraph()

    # read in data for the graph here
    g.addEdge('a',10,'c')
    g.addEdge('c',10,'d')
    g.addEdge('d',10,'f')
    # call a function here
    print(shortestPath(g,'a','f'))
    print("done")
