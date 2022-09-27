# Leetcode 1: Two Sum

- [Link to Problem](https://leetcode.com/problems/two-sum/)


## Solution
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int len = nums.length;
        for (int i = 0; i < len; i += 1) {
            int num = nums[i];

            if (numMap.containsKey(target - num)) {
                return new int[]{numMap.get(target - num), i};
            }

            numMap.put(num, i);
        }

        return new int[]{};
    }
}
```
