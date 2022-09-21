# Leetcode 49: Group Anagrams

- [Link to Problem](https://leetcode.com/problems/group-anagrams/)


## Solution
```java
class Solution {
    public String longestPalindrome(String s) {
        int len = s.length(); // 4

        // i = 4 // j = 0, j + 4 <= 4
        // i = 3 // j = 0, j + 3 <= 4
        // i = 2 // j = 0, j + 2 <= 4
        for (int i = len; i > 0; i--) {
            for (int j = 0; j + i <= len; j++) {
                String subStr = s.substring(j, j+i);
                String[] chars = subStr.split("");
                int lastIndex = chars.length - 1;
                int half = lastIndex / 2;
                boolean isPalindrome = true;
                for (int k = 0; k <= half; k++) {
                    if (!chars[k].equals(chars[lastIndex - k])) {
                        isPalindrome = false;
                        break;
                    }
                }
                if (isPalindrome) {
                    return subStr;
                }
            }
        }

        return s;
    }
}
```
