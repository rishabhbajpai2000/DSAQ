# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        l, cur_ind = 1, 1
        dummy, first = head, head
        
        while dummy.next != None:
            l+= 1
            cur_ind += 1
            dummy = dummy.next
            if cur_ind == k: first = dummy

        
        if l == 1: return head
        
        second = head
        cur_ind = 1
        
        while second.next != None and cur_ind != l - k+1:
            second = second.next
            cur_ind += 1

        first.val, second.val = second.val, first.val
        return head