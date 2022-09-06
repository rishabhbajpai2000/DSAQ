```
class Solution {
public char findKthBit(int n, int k) {
char c = find(n, k, 0, "");
return c;
}
​
private static char find(int n, int k, int i, String string) {
​
if (i == n) {
return string.charAt(k-1);
}
if (i == 0) string = "0";
else string = string + "1" + reverse(invert(string));
return find(n, k, i + 1, string );
}
​
private static String reverse(String invert) {
String ans = "";
for (int i = invert.length() - 1; i > -1; i--)
ans = ans + invert.charAt(i);
​
return ans;
}
​
private static String invert(String string) {
​
String ans = "";
for (int i = 0; i < string.length(); i++) {
if (string.charAt(i) == '0')
ans = ans + '1';
else
ans = ans + '0';
}
​
return ans;
}
}
```