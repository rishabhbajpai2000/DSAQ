# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head
        arr = []
        dummy = head
        while dummy != None:
            arr.append(dummy.val)
            dummy = dummy.next
        arr.sort()
        print(arr)
        dummy = head
        for i in arr:
            dummy.val = i
            dummy = dummy.next
        return head