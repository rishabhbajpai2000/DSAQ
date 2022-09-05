class Solution {
    public int distributeCandies(int[] candyType) {
      
        int l=candyType.length/2;
        Set<Integer> set = new HashSet<Integer>();
        // set.size()=l/2; 
        for(int i=0;i<candyType.length;i++)
        {
            set.add(candyType[i]);
        }
        if(l<set.size())return l;
        return set.size();
    }
}