간# 코딩테스트 연습 > 힙 > 이중우선순위큐

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42628)

## Solution
minQ 와 maxQ를 만든다. 

operation이 I 일 경우, minQ와 maxQ에 값을 넣는다.
operation이 D 1 일 경우, maxQ에서 값을 꺼내서 minQ에서도 제거한다.
operation이 D -1 일 경우, minQ에서 값을 꺼내서 maxQ에서도 제거한다.
마지막으로 maxQ와 minQ에서 값을 꺼내서 answer에 넣는다.

```java
import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minQ = new PriorityQueue<>();
        PriorityQueue<Integer> maxQ = new PriorityQueue<>((a, b) -> b - a);

        for (String op : operations) {
            if (op.equals("D 1")) {
                if (!maxQ.isEmpty()) {
                    int max = maxQ.poll();
                    minQ.remove(max);
                }
            } else if (op.equals("D -1")) {
                if (!minQ.isEmpty()) {
                    int min = minQ.poll();
                    maxQ.remove(min);
                }
            } else {
                int num = Integer.parseInt(op.split(" ")[1]);
                minQ.add(num);
                maxQ.add(num);
            }
        }

        int[] answer = new int[2];
        answer[0] = maxQ.peek() == null ? 0 : maxQ.peek();
        answer[1] = minQ.peek() == null ? 0 : minQ.peek();

        return answer;
    }
}
```


## 시간복잡도와 공간복잡도
- 모르겠음

