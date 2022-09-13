class Solution {
    public int findTheWinner(int n, int k) {
        ArrayList<Integer> arraylist = new ArrayList<>();
        for (int i = 1; i < n+1; i++) {
            arraylist.add(i);
        }
        int ans = helper(arraylist, k, 0);
        return ans;
    }

    private static int helper(ArrayList<Integer> arraylist, int k, int current_pos) {
        if (arraylist.size() == 1) return arraylist.get(0);

        // calculating the next removal position 
        for (int i = 0; i < k-1; i++) {
           current_pos++; 
        }
        current_pos %= arraylist.size();
        System.out.println("Element to be removed is : " + arraylist.get(current_pos));
        arraylist.remove(current_pos);
        return helper(arraylist, k, current_pos);

    }
}