# 코딩테스트 연습 > 스택/큐 > 기능/개발

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42586)

## Solution
배포해야 할 아이템의 배포일을 계산하고, 뒤 따르는 아이템 중 배포가능한 것을 찾는다.  

```java
import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> l = new ArrayList<>();

        // 시간복잡도 O(n), 공간복잡도 O(n)
        for (int i = 0; i < progresses.length;) {
            // 배포일 계산
            double dt = Math.ceil((100.0 - progresses[i]) / speeds[i]);
            int date = (int) Math.ceil(dt);

            int count = 0; // date 날짜에 배포할 수 있는 아이템 수
            while (i < progresses.length && progresses[i] + speeds[i] * date >= 100) {
                count += 1;
                i += 1;
            }
            i -= 1; // 마지막꺼는 while문 조건을 만족하지 않는 애라 -1 해준다.

            l.add(count);
        }

        int[] answer = new int[l.size()];
        for (int i = 0; i < l.size(); i += 1) {
            answer[i] = l.get(i);
        }
        return answer;
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: 평균 O(n)
- 공간복잡도: O(n)

## 참고 자료

### Integer division in floating point context.
`double d = 100/2;`와 같이 int/int가 아닌 float/float 또는 double/double을 하라고 하는 것
이렇게 고치면 된다.
```
double d = 100f/2;
doubld d = 100d/2;
double d = 100.0/2;
```

### 스택/큐

| 시간복잡도(평균) |        |     |          | 시간복잡도(최악) |        |           |          | 공간복잡도 |
|-----------|--------|-----|----------|-----------|--------|-----------|----------|-------|
| Access    | Search | Insertion | Deletion | Access    | Search | Insertion | Deletion |       |
| O(n)      | O(N)   | O(1)      | O(1)     | O(n)      | O(n)   | O(1)      | O(1)     | O(n)  |

- 스택/큐는 접근, 검색을 위해 pop() 또는 poll()을 사용해서 순서대로 다 빼내야해서 O(n)
- 삽입/삭제는 바로바로 되니까 O(1)