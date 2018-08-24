from collections import deque
import Queue

class Frontier:

    """An explicit queue - FIFO. A container for nodes 
    that have been found in the search tree"""
        
    def __init__(self):
        self.queue = deque()

    def __contains__(self, item):
        """Custom method. Search only `state` properties of members"""

        for element in self.queue:
            if item.state == element.state:
                return True

        return False



class Explored:

    """A stack - LIFO. A container for nodes that have already been explored"""
       
    def __init__(self):
        self.set = set()

    def __contains__(self, item):
        """Custom method. Search only `state` properties of elements"""

        for element in self.set:
            if item.state == element.state:
                return True

        return False

        
# TODO: this whole difference between Frontier and Priority_Frontier is a messy hack   
class Priority_Frontier:

    """A priority queue. Position of elements is determined by heuristic"""
        
    def __init__(self):
        self.queue = Queue.PriorityQueue()

    def __contains__(self, item):
        """Custom method. Search only `state` properties of elements"""
        
        for element in self.queue:
            if item.state == element.state:
                return True

        return False
        
