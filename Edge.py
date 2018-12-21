'''
Edge class
'''
class Edge:

    '''
    Constructor for an Edge object
    Essentially a Pair<label,to>
    Immutable with __

    @param label : label of this edge
    @param to : the Node value that the edge is directed to
    '''
    def __init__(self, label, to):
        self.__label = label
        self.__to = to

    '''
    Get the Edge label

    @returns self.__label
    '''
    def getLabel(self):
        return self.__label

    '''
    Get the Directed to edge

    @returns self.__to
    '''
    def getNext(self):
        return self.__to


    '''
    String representation of Edge object for print

    @returns "<label> <to>"
    '''
    def __str__(self):
        return str(self.__label)+ ' ' + str(self.__to)



    '''
    TODO: checkRep()

    '''
    def checkRep(self):
        print("checking rep")




