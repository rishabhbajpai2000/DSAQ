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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode();
        ListNode dummy = ans;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0){
            int v1 = 0;
            int v2 = 0;
            if (l1 != null) v1 = l1.val;
            if (l2 != null) v2 = l2.val;
            
            int sum = v1 + v2 + carry;
            carry = sum/10;
            sum = sum%10;
            dummy.next = new ListNode(sum);
            
            dummy = dummy.next;
            if (l1 != null) l1 = l1.next;
            else l1 = null;
            
            if (l2 != null) l2 = l2.next;
            else l2 = null;
        }
        return ans.next;
    }
}