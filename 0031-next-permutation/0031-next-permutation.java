class Solution {
    public static void reverseArray(int[] arr, int startIndex) {
        int endIndex = arr.length - 1;
        while (startIndex < endIndex) {
            int temp = arr[startIndex];
            arr[startIndex] = arr[endIndex];
            arr[endIndex] = temp;
            startIndex++;
            endIndex--;
        }
    }
  public void nextPermutation(int[] nums) {
    int l = nums.length;
    int index = -1;
      
    for (int i = l - 2; i >= 0; i--) {
      if (nums[i] < nums[i + 1]) {
        index = i;
        break;
      }
    } //correct
      
      
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
      
  reverseArray(nums, index+1);

  }

}
