# Leetcode 0: Name of Problem

- [Link to Problem]()


## Solution1

```java
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    // 대기 중 Queue가 있고,
    // 이동 중 Queue는 다리의 길이만큼 있음, 이동 중인 무게합이 있음

    // 대기중 Queue가 빌 때까지 반복문을 돈다.
    // ㄴ 시간이 1 증가한다.
    // ㄴ 이동 중 Queue 한 칸씩 앞으로 이동한다.
    // ㄴ poll:
    //    ㄴ 트럭이면 이동 중인 무게합 -
    //    ㄴ 트럭이 아니면 그대로
    // ㄴ add: 새로 넣을 수 있는 지 판단한다: 이동 중 무게합 + new < weight
    //    ㄴ 새로 넣을 수 있으면: q.add(), 이동 중 무게합 ++
    //    ㄴ 새로 넣을 수 없으면: q.add(0)

    // 이동중 Queue가 빌 때까지 반복문
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int weightSum = 0;
        Queue<Integer> qWaiting = new LinkedList<>();
        for (int truckWeight : truck_weights) {
            qWaiting.add(truckWeight);
        }
        Queue<Integer> qCrossing = new LinkedList<>();
        for (int i = 0; i < bridge_length; i++) {
            qCrossing.add(0);
        }

        int answer = 0;
        while (!qWaiting.isEmpty()) {
            answer += 1;

            // 뺀다.
            int truckOut = qCrossing.remove();
            weightSum -= truckOut;

            if (weightSum + qWaiting.element() <= weight) {
                int truckIn = qWaiting.remove();
                qCrossing.add(truckIn);
                weightSum += truckIn;
            } else {
                qCrossing.add(0);
            }
        }

        answer += bridge_length;

        return answer;
    }
}
```

## 시간복잡도와 공간복잡도

## Solution2

## 참고자료