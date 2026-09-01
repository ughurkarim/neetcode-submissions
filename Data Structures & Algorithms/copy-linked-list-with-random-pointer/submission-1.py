"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        oldToNew = {}
        
        while curr:
            node = Node(curr.val)
            oldToNew[curr] = node
            curr = curr.next

        curr = head
        while curr:
            newNode = oldToNew[curr]
            if curr.next:
                newNode.next = oldToNew[curr.next]
            else:
                newNode.next = None
            
            if curr.random:
                newNode.random = oldToNew[curr.random]
            else:
                newNode.random = None
            curr = curr.next

        return oldToNew[head]