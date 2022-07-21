/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode s = head;
        ListNode f = head;

        while (f != null && f.next != null) {
            s = s.next;
            f = f.next.next;
        }
        return s;
    }
        public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode prev = null;
        ListNode present = head;
        ListNode next = present.next;

        while (present != null) {
            present.next = prev;
            prev = present;
            present = next;
            if (next != null) {
                next = next.next;
            }
        }
        return prev;
    }
    public void reorderList(ListNode head) {
        // basic check 
        if (head == null) return;
        
        // we are going to reverse the second half of the ll
        ListNode mid = middleNode(head);
        ListNode hs = reverseList(mid);
        
        
        // then are going to make the adjustments according to the conditions
        while (head!= null && hs != null){
            ListNode temp = head.next;
            head.next = hs;
            head = temp;
            
            temp = hs.next;
            hs.next = head;
            hs = temp;
        }
        
        if(head!=null) head.next = null;
    }
}