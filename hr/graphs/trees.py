"""Trees related challenges"""

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def checkBST(root):
    sentinel = None
    min = sentinel
    node = root
    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()

            if min == sentinel:
                min = node.data
            elif min < node.data:
                min = node.data
            else:
                return False

            node = node.right

    return True
