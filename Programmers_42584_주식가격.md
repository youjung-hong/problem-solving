# Programmers 42584: 주식가격

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42584)


## Solution1 - brute force
- 순회하면서 +1씩 해준다. 나보다 작은 값이 나오면 순회를 멈춘다.

```java
// brute force 방법
// 순회하면서 나보다 크면 + 1
//          나보자 작으면 스톱.

class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];

        for (int i = 0; i < len; i += 1) {
            int price = prices[i];
            int time = 0;
            for (int j = i + 1; j < len; j += 1) {
                time += 1;

                if (prices[j] < price) {
                    break;
                }
            }

            answer[i] = time;
        }

        return answer;
    }
}
```

### 시간복잡도와 공간복잡도
- 시간복잡도: O(n^2)
- 공간복잡도: O(n)

## Solution2 - Stack
- 순회하면서
  - stack에 있는 값이 현재값보다 값이 크면, stack에서 빼서 기간을 계산한다. 
  - 현재값을 stack에 넣는다.
- 끝까지 살안남은 것들의 기간을 계산한다.
```java
import java.util.Stack;

class Node {
    int idx;
    int value;

    public Node(int idx, int value) {
        this.idx = idx;
        this.value = value;
    }
}

class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];

        Node[] priceNodes = new Node[len];
        for (int i = 0; i < len; i += 1) {
            priceNodes[i] = new Node(i, prices[i]);
        }

        Stack<Node> stack = new Stack<>();
        stack.push(priceNodes[0]);
        for (int i = 1; i < len; i += 1) {
            Node currentNode = priceNodes[i];
            // 현재값보다 더 큰 것들은 stack에서 빼서 기간을 계산한다.
            while (!stack.isEmpty() && stack.peek().value > currentNode.value) {
                Node node = stack.pop();
                answer[node.idx] = currentNode.idx - node.idx;
            }
            stack.push(currentNode);
        }

        // 끝까지 살아남은 것들의 기간을 계산한다.
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            answer[node.idx] = (len - 1) - node.idx;
        }

        return answer;
    }
}
```

### 시간복잡도/공간복잡도
- 시간복잡도: O(n)
- 공간복잡도: O(n)

## 참고자료