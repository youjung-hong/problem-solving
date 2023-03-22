# 코딩테스트 연습 > 스택/큐 > 올바른 괄호

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/12909)

## Solution
열림이면 stack에 추가, 닫힘이면 stack에서 뺀다. 
만약 stack이 비어있는데 닫힘이면 false,
최종적으로 stack이 비어있어야 true이다.

```java
import java.util.Stack;

class Solution {
    boolean solution(String s) {
        // 열림이면, stack에 추가
        // 닫힘이면 stack에서 뺀다.

        // stack이 빈 값이면 true;
        char open = '(';
        char close = ')';

        char[] chars = s.toCharArray();
        if (chars[0] == close) {
            return false;
        }

        Stack<Character> stack = new Stack<>();
        for (char c : chars) { // O(n)
            if (c == open) {
                stack.add(c); // O(1)
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop(); // O(1)
            }
        }

        return stack.isEmpty();
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: 평균 O(n)
- 공간복잡도: O(n)

## 참고 자료

### 스택/큐

| 시간복잡도(평균) |        |     |          | 시간복잡도(최악) |        |           |          | 공간복잡도 |
|-----------|--------|-----|----------|-----------|--------|-----------|----------|-------|
| Access    | Search | Insertion | Deletion | Access    | Search | Insertion | Deletion |       |
| O(n)      | O(N)   | O(1)      | O(1)     | O(n)      | O(n)   | O(1)      | O(1)     | O(n)  |

- 스택/큐는 접근, 검색을 위해 pop() 또는 poll()을 사용해서 순서대로 다 빼내야해서 O(n)
- 삽입/삭제는 바로바로 되니까 O(1)