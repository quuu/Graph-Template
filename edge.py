'''
Edge class
'''
class Edge:

    # constructor for edge
    def __init__(self, label, to):
        self.__label = label
        self.__to = to

    # accessor for edge label
    def getLabel(self):
        return self.__label

    # accessor for next node
    def getNext(self):
        return self.__to


    def __str__(self):
        return str(self.__label)+ ' ' + str(self.__to)







