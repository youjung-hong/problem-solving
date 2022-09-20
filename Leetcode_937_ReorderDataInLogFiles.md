# Leetcode 937: Reorder Data in Log files

- [Link to Problem](https://leetcode.com/problems/reorder-data-in-log-files/)

```java
List<String> digits = new ArrayList<>();
Map<String, List<String>> letters = new HashMap<>();

for (int i = 0; i < logs.length; i += 1) {

    String[] log = logs[i].split(" ", 2);
    if (log[1].substring(0, 1).matches("\\d")) {
        digits.add(logs[i]);
    } else {
        List<String> values = letters.getOrDefault(log[1], new ArrayList<>());
        values.add(logs[i]);
        letters.put(log[1], values);
    }
}

List<String> data = letters.keySet().stream().sorted()
        .flatMap(key -> letters.get(key).stream().sorted()).collect(Collectors.toList());
data.addAll(digits);

return data.toArray(new String[0]);
```
