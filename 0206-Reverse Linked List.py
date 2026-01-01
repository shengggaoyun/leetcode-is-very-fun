# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        node = head
        nextNode = head.next
        node.next = None

        while nextNode:
            temp = nextNode.next
            nextNode.next = node
            node = nextNode
            nextNode = temp

        return node
