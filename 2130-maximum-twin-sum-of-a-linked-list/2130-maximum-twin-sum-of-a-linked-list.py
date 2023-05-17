# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # counting the length of the list first. 
        l = 1
        dummy = head
        while dummy.next!=None:
            l += 1
            dummy = dummy.next
        maxsum = 0
        dummy = head
        cur_nod_ind = 1
        stack = []
        while dummy != None:
            if cur_nod_ind < l//2 + 1:
                stack.append(dummy.val)
            else:
                maxsum = max(stack[-1] + dummy.val, maxsum)
                stack.pop()
                
            cur_nod_ind += 1
            dummy = dummy.next
                

        return maxsum