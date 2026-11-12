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
        
        # create a hashmap that mapes the old list nodes to new created nodes
        # two pass
        # first pass just creates the copy nodes no connections pointers
        # the second pass connects the pointers 


        oldToNew = {None : None} # map NULL to NULL edge case

        curr = head
        while curr: # first pass creating copy nodes
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        # now need connect pointers
        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]




        