/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) return null;
        
        // we will count the length of the cycle
        // store it in len
        ListNode fast = head;
        ListNode slow = head;
        int len = 0;
        while (fast!= null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            len++;
            if (fast == slow) break;
        }
        System.out.println(len);
        // both fast and slow start at head
        // we increment the fast by len times
        fast = head;
        slow = head;
        while (len > 0){
            fast = fast.next;
            len--;
        }
        
        System.out.println(fast.val);
        
        while (fast != slow){
            if (fast == null || fast.next == null) return null;
            fast = fast.next;
            slow = slow.next;
        }
        return fast;
    }
}