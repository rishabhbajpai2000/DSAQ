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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return null;
        ListNode temp = head;
        
        int len = 1;
        while (temp.next != null){
            temp = temp.next; 
            len++;
        }
        temp.next = head;
        
        int h_ind = len - k%len;
        ListNode n = head;
        for (int i = 0; i<h_ind-1; i++){
            n = n.next;
        }
        
        head = n.next;
        n.next = null;
        return head;
        
    }
}