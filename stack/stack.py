"""
Module implements data structure class for stack
"""
class Stack(object):
    """
    Class of list of
    """
    def __init__(self, numberOfElements=0):
        """
        Initializes the list/array of numberOfElements zeros
        """
        self.data = [0]*numberOfElements

    def push(self, value):
        """
        Adds value to end of the list
        """
        self.data.append(value)
        return 0

    def pop(self):
        """
        Removes last element from the list
        """
        del self.data[-1]
        return 0

    def show(self):
        """
        Prints the list in one line
        """
        print '[',
        for elem in self.data:
            print(elem),
        print ']'
