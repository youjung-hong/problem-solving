간# 코딩테스트 연습 > 정렬 > 가장 큰 수

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42746)

## Solution1
- 숫자를 문자열로 변환한다.
- 정렬한다: `${b}{a}` > `${a}{b}` 이면 합쳤을 때 더 큰 b가 앞에 오도록 정렬한다.


```java
import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        int len = numbers.length;
        String[] numstrs = new String[len];

        for (int i = 0; i < len; i += 1) {
            numstrs[i] = String.valueOf(numbers[i]);
        }

        // `${b}{a}` > `${a}{b}` 이면 합쳤을 때 더 큰 b가 앞에 오도록 정렬한다.
        Arrays.sort(numstrs, (a, b) -> b.concat(a).compareTo(a.concat(b)));
        
        String answer = String.join("", numstrs);
        if (answer.charAt(0) == '0') { // 예외
            return "0";
        }

        return answer;
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: O(nlogn)
- 공간복잡도: O(n)

## 참고 자료

### 풀면서 든 생각
알고리즘은 갖다 쓰는 거구만...
그래도 알고리즘을 어떻게 구현하는 지는 꼭 알아야 하니까 알아두자.