class Solution {
    public int addDigits(int num) {
        if (num<10) return num;
        
        int s = 0;
        while (num > 0){
            int rem = num%10;
            s += rem;
            num/=10;
        }
        
        return addDigits(s);
    }
}