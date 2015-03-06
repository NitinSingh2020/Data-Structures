"""
Author     : Nitin Singh
Dependency : stack.py
Execution  : python testRunner.py
"""

from stack import Stack

if __name__ == "__main__":
    stack1 = Stack(3)
    stack1.show()
    stack1.push(2)
    stack1.show()
    stack1.pop()
    stack1.show()
    print "stack-1 created"