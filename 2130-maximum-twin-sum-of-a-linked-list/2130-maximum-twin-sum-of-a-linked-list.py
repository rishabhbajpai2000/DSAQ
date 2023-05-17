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
        cur_nod_ind = 1
        stack = []
        while head != None:
            if cur_nod_ind < l//2 + 1:
                stack.append(head.val)
            else:
                maxsum = max(stack.pop()+ head.val, maxsum)
                
            cur_nod_ind += 1
            head = head.next
                

        return maxsum