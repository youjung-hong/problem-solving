# Leetcode 344: Reverse String

- [Link to Problem](https://leetcode.com/problems/reverse-string/))


## Solution
```java
class Solution {
    public void reverseString(char[] s) {
        // hell
        // 0-3, 1-2 // 1

        // hello
        // 0-4, 1-3 // 2
        int lastIndex = s.length - 1;
        int half = lastIndex / 2;
        char temp;
        for (int i = 0; i <= half; i += 1) {
            temp = s[i];
            s[i] = s[lastIndex - i];
            s[lastIndex - i] = temp;
        }
    }
}
```
