My code
```
class Solution {
public int firstMissingPositive(int[] nums) {
//making a hash table and inputting every positive element in that
int[] hash = new int[nums.length+1];
for(int elem:nums){
if(elem>=0 && elem<= nums.length){
hash[elem] = 1;
}
}
// now checking for missing element from the hash table
for(int i = 1; i<hash.length;i++){
if (hash[i] != 1){
return i;
}
}
return hash.length;
}
}
```