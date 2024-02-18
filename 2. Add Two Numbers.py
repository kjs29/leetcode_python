# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()   # create empty headnode
        curr = head         # we will work with curr
        carry = 0           # indicates a carry over if sum exceeds 10
        
        while l1 or l2 or carry:                # if one of them is true, continue
            val1 = l1.val if l1 else 0          # we will work with value, since None does not have ".val"
            val2 = l2.val if l2 else 0          # we will work with value, since None does not have ".val"
            total = val1 + val2 + carry
            
            curr.next = ListNode(total % 10)    # get the ones place (1의자리)
            curr = curr.next                    # update curr to curr.next
            
            carry = total // 10                 # update carry
            l1 = l1.next if l1 else None        # update l1, if not existing, assign None
            l2 = l2.next if l2 else None        # update l2, if not existing, assign None

        return head.next    # since the first head node's val is 0, return head.next