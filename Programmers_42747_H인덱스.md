간# 코딩테스트 연습 > 정렬 > H-index

- [Link to Problem](https://programmers.co.kr/learn/courses/30/lessons/42747))

## Solution

| Solution |    |
|----|----|
| ![Programmers Solutions 정렬-2](https://user-images.githubusercontent.com/13758710/232515202-ba251c57-8c30-42e0-a860-5f4560ec41cc.jpg) | ![Programmers Solutions 정렬-3](https://user-images.githubusercontent.com/13758710/232515221-80e72a84-0f70-4dc7-ac4f-4e91bb4f2216.jpg)  |


```java
import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);

        int n = citations.length;

        for (int i = 0; i <= n/2; i += 1) {
            int h = n - i;
            if (citations[i] >= h) {
                return h;
            }
        }

        return 0;
    }
}
```

