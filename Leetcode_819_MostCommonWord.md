# Leetcode 819: Most Common Word

- [Link to Problem](https://leetcode.com/problems/most-common-word/submissions/)


## Solution
```java
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Map<String, Integer> wordCountMap = new HashMap<>();
        Set<String> bannedSet = new HashSet<>(List.of(banned));
        List<String> words = Arrays.stream(paragraph.replaceAll("[!?',;.]", " ").toLowerCase().split(" "))
                .filter(word -> !bannedSet.contains(word) && !word.isEmpty()).collect(Collectors.toList());

        String mostFrequentWord = "";
        int mostFrequentWordCount = 0;
        for (String word : words) {
            wordCountMap.put(word, wordCountMap.getOrDefault(word, 0) + 1);

            if (wordCountMap.get(word) > mostFrequentWordCount) {
                mostFrequentWord = word;
                mostFrequentWordCount = wordCountMap.get(word);
            }
        }

        return mostFrequentWord;
    }
}
```
