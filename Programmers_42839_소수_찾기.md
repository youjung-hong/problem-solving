간# 코딩테스트 연습 > 완전탐색 > 소수 찾기

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42839)

## Solution
순열 찾기 -> 소수 판별 -> 소수 갯수 반환

순열 찾기 구현,, 소수 판별하는 법 모두 정답을 참고했다.

```java
import java.util.*;

class Solution {
    private Map<Integer, Boolean> primeMap = new HashMap<>();

    public int solution(String numbers) {

        // 1. 숫자 조합
        HashSet<Integer> set = new HashSet<>();
        permutation("", numbers, set);

        // 2. 소수 판별
        for (int num : set) {
            primeMap.put(num, isPrime(num));
        }

        // 3. 소수 개수 반환
        return (int) primeMap.values().stream().filter(it -> it).count();
    }

    private void permutation(String prefix, String str, HashSet<Integer> set) {
        if (!prefix.equals("")) {
            set.add(Integer.valueOf(prefix));
        }

        int n = str.length();
        for (int i = 0; i < n; i++) {
            // i번째 문자를 붙이고, 나머지 문자들만 넘겨준다.
            permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n), set);
        }
    }

    private boolean isPrime(int num) {
        if (num == 0 || num == 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) { // 나누어 떨어지면 소수가 아님
                return false;
            }
        }

        return true;
    }
}
```

## 시간복잡도와 공간복잡도


## 참고 자료

