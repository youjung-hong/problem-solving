# Leetcode 125: Valid Palindrome

- [Link to Problem](https://leetcode.com/problems/valid-palindrome/)


## Solution
```java
class Solution {
    public boolean isPalindrome(String s) {
        // Split into half, and compare the front one and the last one

        s = s.replaceAll("[^A-Za-z0-9]", "");
        s = s.toLowerCase();
        
         if (s.isEmpty()) {
            return true;
        }

        // 0, 1, 2, 3 // 0, 1, 2, 3, 4
        int lastIndex = s.length() - 1; // 3 // 4
        int half = lastIndex / 2; // 1 // 2

        for(int i = 0; i <= half; i += 1) { // 0-3, 1-2 // 0-4, 1-3, 2-2
            if (s.charAt(i) != s.charAt(lastIndex - i)) {
                return false;
            }
        }

        return true;
    }
}
```
