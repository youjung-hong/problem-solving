간# 코딩테스트 연습 > 힙 > 디스크 컨트롤러

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42627)

## Solution
현재 시간이 요청시간 이후이거나 같은 것만 먼저 큐에 넣고, 그 중에서 소요시간이 가장 짧은 것을 먼저 처리한다.
만약, 대기 중인 잡이 있는 데, 현재 시점에 큐가 비어있는 경우 현재 시점을 다음에 요청이 들어올 시점으로 변경한다.
모든 잡이 처리될 때까지 반복한다.

```java
import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        // 1. jobs 배열을 요청시간을 기준으로 오름차순 정렬한다. 
        Arrays.sort(jobs, Comparator.comparingInt(o -> o[0]));

        // 2. 소요시간이 짧은 것을 우선순위로 하는 우선순위 큐를 생성
        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(o -> o[1]));

        int time = 0;
        int i = 0;
        int answer = 0;
        int count = 0;

        // 3. jobs 배열을 순회하면서, 요청시간이 작거나 같은 것을 먼저 우선순위 큐에 넣는다.
        while (count < jobs.length) {
            for (; i < jobs.length; i += 1) {
                int[] job = jobs[i];
                if (job[0] <= time) { // 3.1 현재 시간 이전 또는 현재 시간에 요청이 들어온 경우 우선순위 큐에 넣는다.
                    queue.add(job);
                } else {
                    break;
                }
            }

            if (queue.isEmpty()) { // 3.2 우선순위 큐가 비어있는 경우, 현재 시간을 다음에 요청이 들어올 시간으로 변경한다.
                time = jobs[i][0];
                continue;
            }

            int[] job = queue.poll(); // 3.3 소요시간이 가장 짧은 작업을 꺼낸다.
            answer += job[1] + (time - job[0]); // 소요시간과 대기 시간을 합한다. 
            time += job[1];
            count += 1;
        }

        return answer / count;
    }
}
```


## 시간복잡도와 공간복잡도
- 모르겠음

