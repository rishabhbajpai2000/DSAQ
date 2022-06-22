class Solution {
    public double myPow(double x, int n) {        
        double pow = helper(x, Math.abs(n));
        if (n<0)
            return 1/pow;
        return pow;
    }
    
    double helper(double x, int n){
        if (x == 0) return 0;
        if (n == 0) return 1;
        double res = helper(x, n/2);
        res = res*res;
        if (n%2 != 0)
            return x*res;
        else
            return res;
        
    }
}