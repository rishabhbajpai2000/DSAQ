```
//solution 1
if (n == 0) return;
if (m == 0 && n==1) nums1[0] = nums2[0];
for (int i = m; i<m+n; i++)
nums1[i] = nums2[i-m];
Arrays.sort(nums1);
```
​
Approach 2 - not working
```
class Solution {
public void merge(int[] nums1, int m, int[] nums2, int n) {
// copying the elements of second in first;
for (int i = m; i<m+n; i++)
nums1[i] = nums2[i-m];
int gap = (int)Math.ceil(((float)m+n)/2);
​
do{
int first = 0;
int second = gap-1;
if (nums1[first] > nums1[second])
interchange(nums2, first, second);
first++;
second++;
if (second==m+n){
gap = gap/2;
continue;
}
}
while (gap != 1);
}
static void interchangte(int[] arr, int first, int second){
int temp = arr[first];
arr[first] = arr[second];
arr[second] = temp;
}
```