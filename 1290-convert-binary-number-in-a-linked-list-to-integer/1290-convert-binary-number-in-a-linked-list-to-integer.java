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
    public int getDecimalValue(ListNode head) {
        ListNode temp = head;
        // calculating the size of list
        int size = 1;
        while (temp.next != null){
            temp = temp.next;
            size++;
        }
        System.out.println("size = " + size);
        // calculating the value as 2 ^size
        int pow = 1;
        for (int i = 1; i<size;i++){
            pow *= 2;
        }
        // System.out.println("power = " + pow);
        temp =head;
        int ans = 0;
        while (size >0){
            ans += pow * temp.val;
            // System.out.println("ans = "+ ans);
            // System.out.println("temp.val = "+ temp.val);
            pow /= 2;
            size--;
            temp = temp.next;
            // System.out.println("power = " + pow);
        }
        return ans;
        
    }
}