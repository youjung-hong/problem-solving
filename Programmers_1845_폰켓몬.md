# 코딩테스트 연습 > 해시 > 폰켓몬

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/1845)

## Solution
`min(nums 배열 속 유니크한 숫자의 갯수, N/2)`가 정답이다.
nums 배열 속 유니크한 숫자의 갯수를 구하기 위해 Set을 사용하였다.
Set은 중복을 허용하지 않도록 데이터를 저장하기 때문이다.

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    // 시간 복잡도 - 평균 O(1), 최악 O(n)
    // 공간 복잡도 - O(n)
    public int solution(int[] nums) {
        Set<Integer> set = new HashSet<>();
        // 1. 해시 테이블 추가 시간 복잡도: 평균 O(1), 최악 O(n)
        for (int num : nums) {
            set.add(num);
        }
        return Math.min(set.size(), nums.length / 2);
    } // 총 시간 복잡도: O(1), 총 공간 복잡도: O(n)
}
```

## 시간복잡도와 공간복잡도
해시 테이블 추가가 가장 복잡도가 큰 연산이다.
- 시간복잡도: 평균 O(1), 최악 O(n)
- 공간복잡도: O(n)

## 참고 자료

### Java의 Set 구현체별 특징 - 순서보장 특징이 다름
- HashSet: 유니크한 데이터 저장 + 순서보장 없음
- LinkedHashSet: 유니크한 데이터 저장 + 입력된 순서대로 저장
- TreeSet: 유니크한 데이터 저장 + 데이터의 오름차순으로 저장

### 해시 테이블

| 시간복잡도(평균) |        |     |          | 시간복잡도(최악) |        |           |          | 공간복잡도 |
|-----------|--------|-----|----------|-----------|--------|-----------|----------|-------|
| Access    | Search | Insertion | Deletion | Access    | Search | Insertion | Deletion |       |
| N/A       | O(1)   | O(1)      | O(1)     | O(n)      | O(n)   | O(n)      | O(n)     | O(n)  |

- 해시 테이블은 같은 해시키를 가진 데이터가 한 개 밖에 없을 경우, O(1)로 접근할 수 있다.
- 같은 해시키를 가진 데이터가 여러 개일 때, 그 목록을 다 뒤져야 하기 때문에, 최악의 경우인 모든 엘리먼트들의 해시키가 같은 경우엔 O(n)이다.
- 공간 복잡도는 엘리먼트가 1개 추가될 때마다 데이터가 늘어나므로 O(n)이다