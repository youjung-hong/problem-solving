# 코딩테스트 연습 > 해시 > 위장

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42578)

## Solution
의상의 종류별 갯수를 구하기 위해 Map을 사용하여 갯수 맵을 만든다. 
경우의 수는 종류별로 의상의 갯수 + 1(아무것도 안 입는 경우 포함)을 곱하고 아무것도 안 선택한 경우 1을 뺀 값이다. 

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();

        for (String[] c : clothes) { // O(n)
            map.put(c[1], map.getOrDefault(c[1], 0) + 1);
        }

        int count = 1;
        for (Integer c : map.values()) { // O(n)
            count = count * (c + 1);
        }

        return count - 1;
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: 평균 O(n)
- 공간복잡도: O(n * m)

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