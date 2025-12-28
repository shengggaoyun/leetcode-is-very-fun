# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    """
    Intuition: Very similar to binary addition. We keep track of the carry and 
    iterate so long as we either have node values in l1, l2 or have carry-over. The resulting
    linked list contains all the remainder.

    Runtime: O(n) where n is the length of the longest linked list between l1 and l2.

    Memory: O(n) to store the resulting linked list. (O(1) considering we only use pointers)

    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        cur1 = l1
        cur2 = l2
        while cur1 or cur2 or carry:
            if cur1:
                value1 = cur1.val
            else:
                value1 = 0
            
            if cur2:
                value2 = cur2.val
            else:
                value2 = 0
            
            sum = value1 + value2 + carry
            carry = sum//10
            remainder = sum % 10
            
            curr.next = ListNode(remainder)
            curr = curr.next

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        return dummy.next

        