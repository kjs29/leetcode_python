# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursive(self, newHead, prev=None):
        """
        Time: O(n)
        Space: O(n) - call stack
        """
        if not newHead:
            return prev
        next = newHead.next
        newHead.next = prev
        return self.recursive(next, newHead)

    def iterative(self, newHead):
        """
        Time: O(n)
        Space: O(1)
        """
        cur = newHead
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def iterative_2(self, newHead):
        """
        Time: O(n)
        Space: O(n)
        """
        cur = newHead
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        dummy = ListNode()
        ans = dummy
        for i in range(len(vals)-1,-1,-1):
            dummy.next = ListNode(vals[i])
            dummy=dummy.next
        return ans.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = self.recursive(head)
        # ans = self.iterative(head)
        # ans = self.iterative_2(head)
        return ans