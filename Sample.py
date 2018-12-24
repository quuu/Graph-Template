

from Graph import *
import heapdict
import heapq
'''
TODO: shortest path from one node to another
given numerical edge labels

@requires __nodes to have edge labels of ints or doubles

@param start : Node(start) to start at
@param end : Node(end) to end at
@return String of path to get from start to end, or that no path is found
'''
def shortestPath(graph, start, end):

    visited = []
    dist = {}
    hd = heapdict.heapdict()
    dist[start]=0
    hd[start]=0


    # main loop
    while (len(hd)):

        '''
        save the path so far in an array 
        containing arrays

        pop minimum item
        compute distance traveled so far
        see if it's a match
            - return
        add all neighbors NOT in visited of popped item
            into the heapdict with the distance traveled
        add popped item to visited list
        '''
        
        # current holds (key, priority)
        current = hd.popitem()
        print(current)

        # if result is found
        if (current[0] is end):
            print('found')
            return
    
        # add all neighbors to the queue
        for e in graph.getNeighbors(current[0]):
            if (not e.getNext() in visited):
                hd[e.getNext()] = e.getLabel()

        # make sure not to revisit
        visited.append(current[0])

    return


if __name__ == '__main__':
    g = DirectedGraph()

    # read in data for the graph here
    g.addEdge('a',1000,'c')
    g.addEdge('a',10,'r')
    g.addEdge('a',10,'t')
    g.addEdge('a',10,'y')
    g.addEdge('c',10,'d')
    g.addEdge('d',10,'f')
    # call a function here
    print(shortestPath(g,'a','f'))
    print("done")
