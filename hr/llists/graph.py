"""
Detect a cycle in a linked list. Note that the head pointer may be
'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def _next_slow(node):
    return None if not node else node.next

def _next_fast(node):
    return _next_slow(_next_slow(node))

def has_cycle(head):
    if not head:
        return False

    it_slow = head
    it_fast = head
    while True:
        it_slow = _next_slow(it_slow)
        it_fast = _next_fast(it_fast)

        if not it_slow or not it_fast:
            return False

        if it_slow == it_fast:
            return True
