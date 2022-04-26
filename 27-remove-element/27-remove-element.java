class Solution {
    public int removeElement(int[] nums, int val) {    
        // replacing every element with value val in nums with integer.minvalue
        int count = 0;
        for (int i  = 0; i<nums.length; i++){
            if (nums[i] == val){
                nums[i] = Integer.MIN_VALUE;
                count++;
            }
        }
        //now sorting the array in decreasing order, used insertion sort
        sort(nums);
        return nums.length - count;
    }

    void sort(int[] nums){
        for (int i = 0; i<nums.length - 1; i++){
            for (int j = i+ 1; j>0; j--){
                if (nums[j-1]<nums[j])
                    swap(nums, j, j-1);
                else
                    break;
            }
                
        }
    }


    void swap(int[] arr, int first,int second){
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}

// now replacing the min values stored inside the array to the end of the array.
        // int end = nums.length-1;
        // for (int i = 0; i<nums.length; i++){
        //     if (nums[end] == Integer.MIN_VALUE){
        //             end--;
        //         }
        //     if (nums[i] == Integer.MIN_VALUE){
        //         nums[i] = nums[end];
        //         end--;
        //     }
            
        