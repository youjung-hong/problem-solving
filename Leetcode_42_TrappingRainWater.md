# Leetcode 42: Trapping Rain Water

- [Link to Problem](https://leetcode.com/problems/trapping-rain-water/)


## Solution
```java
class Solution {
    public int trap(int[] height) {
        int len = height.length;

        int from = 0;
        int to = len - 1;

        int result = 0;

        for(int i = 1; i < len;) {
            int cur = height[i];

            int left = i - 1;
            int right = i + 1;
            while(left > -1 && left >= from) {
                if (height[left] > cur) {
                    break;
                }
                left -= 1;
            }
            while(left != -1 && right < len) {
                if (height[right] > cur) {
                    break;
                }
                right += 1;
            }

            if (left == -1 || right == len) {
                i += 1;
                continue;
            }

            int min = height[left] < height[right] ? height[left] : height[right];
            for(int j = left + 1; j < right; j += 1) {
                result += (min - height[j]);
            }
            from = right + 1;
            i = right + 1;
        }

        return result;
    }
}
```
