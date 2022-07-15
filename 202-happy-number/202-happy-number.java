class Solution {
    public boolean isHappy(int n) {
        int fast = n;
        int slow = n;
       do {
            fast = square(square(fast));
            slow = square(slow);
            System.out.println(fast + " " + slow);
        } while (fast != slow);
        if (fast == 1) return true;
        return false;
    }
    
    int square(int n){
        int s = 0;
        while (n>0 ){
            s += (n%10)*(n%10);
            n = n/10;
        }
        return s;
    }
}