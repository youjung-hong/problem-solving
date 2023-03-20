# 코딩테스트 연습 > 해시 > 베스트앨범

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/12906)

## Solution
순회하면서 마지막에 입력된 값이 현재 값과 비교한다.
같으면 넘어가고, 다르면 list에 추가한다. 
list를 배열로 변환하여 리턴한다.

```java
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> l = new ArrayList<>();
        int prev = -1;

        // 시간복잡도 O(n)
        // 공간복잡도 O(m <= n)
        for (int num : arr) {
            if (prev != num) {
                l.add(num);
                prev = num;
            }
        }

        int[] answer = new int[l.size()];
        for (int i = 0; i < l.size(); i += 1) { // 시간복잡도 O(m), 공간복잡도 O(m)
            answer[i] = l.get(i);
        }

        return answer;
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: O(n) 
- 공간복잡도: O(n)

## 참고 자료
