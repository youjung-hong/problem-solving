간# 코딩테스트 연습 > 완전탐색 > 모의고사

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42840)

## Solution
다 확인함

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] answers) {
        int[] a = new int[]{1, 2, 3, 4, 5};
        int[] b = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        int count_a = 0;
        int count_b = 0;
        int count_c = 0;
        for (int i = 0; i < answers.length; i += 1) {
            if (answers[i] == a[i%5]) count_a ++;
            if (answers[i] == b[i%8]) count_b ++;
            if (answers[i] == c[i%10]) count_c ++;
        }

        int max = Math.max(count_a, count_b);
        max = Math.max(max, count_c);

        List<Integer> anslist = new ArrayList<>();
        if (max == count_a) {
            anslist.add(1);
        }
        if (max == count_b) {
            anslist.add(2);
        }
        if (max == count_c) {
            anslist.add(3);
        }

        int[] answer  = new int[anslist.size()];
        for (int i = 0; i < anslist.size(); i += 1) {
            answer[i] = anslist.get(i);
        }

        return answer;
    }
}
```

## 시간복잡도와 공간복잡도


## 참고 자료

