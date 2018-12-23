

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
    q = []
    visited = []
    heapq.heappush(q,start)

    hd = heapdict.heapdict()
    hd[start]=0


    # main loop
    while(len(hd)):

        '''
        pop minimum item
        compute distance traveled so far
        see if it's a match
            - return
        add all neighbors NOT in visited of popped item
            into the heapdict with the distance traveled
        add popped item to visited list
        '''
        current = heapq.heappop(q)

        #if the result is found
        if(current == end):
            print("found")
            return

        # add all neighbors to the queue
        for e in graph.getNeighbors(current):
            if(not e.getNext() in visited):
                heapq.heappush(q,e.getNext())

        # make sure not to revisit
        visited.append(current)

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
