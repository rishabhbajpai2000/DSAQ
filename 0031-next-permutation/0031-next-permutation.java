class Solution {

  public void nextPermutation(int[] nums) {
    int l = nums.length;
    int index = -1;
      
    for (int i = l - 2; i >= 0; i--) {
      if (nums[i] < nums[i + 1]) {
        index = i;
        break;
      }
    } //correct
    System.out.println(index);
      
      
    if (index == -1) { //reverse
      int x = l - 1;
      for (int i = 0; i < l / 2; i++) {
        int t = nums[i];
        nums[i] = nums[x];
        nums[x] = t;
        x--;
      }
    return;
    } //l=3 i=2 index=1
      
      
    for (int i = l - 1; i >= 0; i--) {
      if (nums[i] > nums[index]) {
        int temp = nums[index];
        nums[index] = nums[i];
        nums[i] = temp;
        break;
      }
    }
    System.out.println(Arrays.toString(nums));
      
    // int z = l - 1; //reverse rest of the part
    // for (int k = index + 1; k <= (l-index)/2; k++) {
    //   int t = nums[k];
    //   nums[k] = nums[z];
    //   nums[z] = t;
    //   z--;
    // }
    Arrays.sort(nums, index+1,l);
      
    System.out.println(Arrays.toString(nums));
  }
}
