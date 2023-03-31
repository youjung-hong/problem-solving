간# 코딩테스트 연습 > 스택/큐 > 프린터

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42587)

## Solution
// 순회하면서
// ㄴ 중요도별로 세고, 가장 높은 중요도를 찾는다.
// ㄴ Priority, index 값을 갖고 있는 인쇄대기아이템을 만든다.
// ㄴ 만든 것을 Queue에 넣는다.

배포해야 할 아이템의 배포일을 계산하고, 뒤 따르는 아이템 중 배포가능한 것을 찾는다.  

```java
import java.util.LinkedList;
import java.util.Queue;

class PrintItem {
    private int priority;
    private int index;

    public PrintItem(int priority, int index) {
        this.priority = priority;
        this.index = index;
    }

    public boolean isMaxPriority(int maxPriority) {
        return this.priority == maxPriority;
    }

    public boolean isTarget(int targetIndex) {
        return this.index == targetIndex;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        // 순회하면서
        // ㄴ 중요도별로 세고, 가장 높은 중요도를 찾는다.
        // ㄴ Priority, index 값을 갖고 있는 인쇄대기아이템을 만든다.
        // ㄴ 만든 것을 Queue에 넣는다.
        int maxPriority = 0;
        int[] priorityCounts = new int[10];
        Queue<PrintItem> printQueue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i += 1) {
            PrintItem printItem = new PrintItem(priorities[i], i);
            priorityCounts[priorities[i]] += 1;
            if (maxPriority < priorities[i]) {
                maxPriority = priorities[i];
            }
            printQueue.add(printItem);
        }


        // Queue가 빌 때까지 반복한다.
        // ㄴ 가장 앞에 있는 문서를 대기목록에서 꺼낸다.
        // ㄴ 가장 중요도가 높으면, 대기 목록에서 빼고 인쇄 횟수를 +1한다. 만약 사용자가 찾는 것이면 인쇄횟수를 반환한다.
        // ㄴ 가장 중요도가 높지 않으면, Queue에 다시 넣는다.
        int answer = 0;
        while (!printQueue.isEmpty()) {
            PrintItem printItem = printQueue.poll();
            if (printItem.isMaxPriority(maxPriority)) {
                answer += 1;
                priorityCounts[maxPriority] -= 1;
                maxPriority = findPriority(priorityCounts, maxPriority);
                if (printItem.isTarget(location)) {
                    return answer;
                }
            } else {
                printQueue.add(printItem);
            }
        }

        return answer;
    }

    private int findPriority(int[] priorityCounts, int maxPriority) {
        for (int i = maxPriority; i > 0; i -= 1) {
            if (priorityCounts[i] > 0) {
                return i;
            }
        }
        return 0;
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