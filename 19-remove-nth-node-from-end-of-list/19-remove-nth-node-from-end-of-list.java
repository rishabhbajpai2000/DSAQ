class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;
        
        int l = 0;
        // getting the length of the list
        ListNode temp = head;
        while (temp != null){
            temp = temp.next;
            l++;
        }
        
        
        // going to the node just before the node which we need to delete. . 
        ListNode L_B_D = head; // lbd =  last before delete
        int ind = l-n-1;     
        
        if(ind>=0){
            for (int i = 0; i<ind ;i++)
                L_B_D = L_B_D.next;
        
        if (L_B_D.next != null) 
            L_B_D.next = L_B_D.next.next;
        
        return head;
        }
        else{
            if (L_B_D.next != null)
                return L_B_D.next;
            else
                return null;
        }        
    }
}