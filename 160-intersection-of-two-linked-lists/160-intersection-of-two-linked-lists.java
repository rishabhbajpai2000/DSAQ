/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;
        
        // getting the length of the linked lists
        int l_a = 1;
        int l_b = 1;
        
        ListNode ta = headA;
        ListNode tb = headB;
        
        while (ta.next!= null){
            ta =  ta.next;
            l_a++;
        }
        while (tb.next!= null){
            tb = tb.next;
            l_b++;
        }
        
        if (l_a > l_b){
            // we need to move to l_a - l_b + 1 node in headA list
            int to_reach = l_a - l_b + 1;
            for (int i = 1; i< to_reach; i++){
                headA = headA.next;
            }
        }
        else{
            // we need to move to l_b - l_a + 1 node in headB list
            int to_reach = l_b - l_a + 1;
             for (int i = 1; i< to_reach; i++){
                 headB = headB.next; 
            }            
        }
        System.out.println(headA.val + " " + headB.val);
        while (headA != null){
            if (headA == headB) return headA;
            headA = headA.next;
            headB = headB.next;
            
            
            
        }
        return null;
    }
}