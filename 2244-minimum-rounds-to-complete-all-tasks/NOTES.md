for(int i = 0; i<tasks.length; i++){
if (tasks[i] == elem){
return i;
}
}
return 0;
}
static int end_ind(int[] tasks, int elem) {
for(int i = tasks.length-1; i>0; i--){
if (tasks[i] == elem){
return i;
}
}
return 0;
}
}
```
​
second solution with memory limit exceeded
```
class Solution {
public int minimumRounds(int[] tasks) {
int rounds = 0;
// finding the max element in the array.
int max = 0;
for (int elem : tasks){
if (elem>max)
max = elem;
}
// making a frequency array
int[] freq = new int[max+1];
for(int elem: tasks){
freq[elem]++;
}
// iterating that frequency array to find the rounds.
for(int elem:freq){
int num = elem;
if (num%3 == 0)
rounds += num/3;
if (num%3 == 1 && num>=4)
rounds += (num-4)/3 + 2;
if (num%3 == 2)
rounds += num/3 + 1;
if (num == 1)
return -1;
}
return rounds;
}
}
```