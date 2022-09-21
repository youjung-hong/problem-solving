# Leetcode 49: Group Anagrams

- [Link to Problem](https://leetcode.com/problems/group-anagrams/)


## Solution
```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            String key = Arrays.stream(str.split("")).sorted().collect(Collectors.joining());
            List<String> value = map.getOrDefault(key, new ArrayList<>());
            value.add(str);
            map.put(key, value);
        }

        return map.values().stream().collect(Collectors.toList());
    }
}
```
