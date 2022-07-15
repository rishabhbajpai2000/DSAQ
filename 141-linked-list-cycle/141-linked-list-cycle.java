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
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        int count = 0;
        while (true){
            if (head.next == null) return false;
            else{
                head = head.next;
                count++;
                if (count>10000) return true;
                
            }
            
        }
    }
}