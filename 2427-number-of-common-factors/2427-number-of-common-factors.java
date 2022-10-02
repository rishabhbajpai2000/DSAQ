class Solution {
    public int commonFactors(int a, int b) {
        int smaller = a;
        int larger = b;
        
        if (a>=b){ 
            larger = a;
            smaller = b;
        }
        int count =0;
        for (int i = 1; i<=smaller; i++)
        {
            if (a%i ==0 && b%i ==0) count++;
        }
        return count;
    }
}