# 코딩테스트 연습 > 해시 > 완주하지 못한 선수

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42576)

## Solution
참가자 목록에서 완주하지 못한 선수를 식별하기 위해 참가자 이름으로 해시 맵을 만들고, 완주한 선수 이름 목록을 순회하면서 맵에서 제외한다. 
참가자 중에는 동명이인이 있을 수 있기 때문에, 맵은 참가자 이름과 동명이인의 수 쌍으로 구성된다. 
완주하지 못한 선수는 항상 한 명이기 때문에 마지막에 남은 키의 값(이름)이 반환해야 할 값이다.

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        // 해시테이블의 삽입, 조회, 삭제에 대한 시간복잡도는 평균의 경우 O(1), 최악의 경우 O(n)이다. 여기서는 평균의 경우만 생각한다.
        Map<String, Integer> map = new HashMap<>();

        // for loop 만큼 순회하는 데 O(n)이 들고, 순회하는 경우 O(1)이라 O(n)*O(1) = O(n) 이다.
        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }

        // 위와 마찬가지로 O(n)이다.
        for (String c : completion) {
            map.put(c, map.get(c) - 1);
            if (map.get(c).equals(0)) {
                map.remove(c);
            }
        }

        // 조건에 따르면, 완주하지 못한 선수는 한 명 밖에 없기 때문에
        // 첫번째 키를 조회하고 따라서 O(1)이다.
        return map.keySet().iterator().next();
        
        // 최종적으로 O(2n + 1) = O(n)이다. 
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: 평균 O(n), 최악 O(n^2)
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