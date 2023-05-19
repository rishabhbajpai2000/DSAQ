# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        l= 1
        dummy = head
        cur_ind = 1
        first = head
        
        while dummy.next != None:
            l += 1            
            cur_ind += 1
            dummy = dummy.next
            if cur_ind == k: 
                print(first.val)
                first = dummy


        print(l, first.val)
        
        if l == 1: return head
        
        second = head
        cur_ind = 1
        
        while second.next != None and cur_ind != l - k+1:
            second = second.next
            cur_ind += 1
        
        print(second.val)
        first.val, second.val = second.val, first.val
        return head