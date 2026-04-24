# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        visited = []
        dummy = ListNode()
        tail = dummy

        while head:
            visited.append(head)
            head = head.next
        
        second = len(visited) - 1
        first = 0
        while first < second:
            visited[first].next = visited[second]
            first+=1
            if first >= second:
                break
            visited[second].next = visited[first]
            second -= 1
        
        visited[first].next = None
            


        # 0, 6, 1, 5, 2, 4, 3
        # 0  n  0  n  0  n  0

        