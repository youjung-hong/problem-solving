# 코딩테스트 연습 > 해시 > 베스트앨범

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

## Solution
순회하면서 장르의 합을 구하고, 같은 장르의 것을 [고유번호, 재생횟수] 묶ㄴㄴ다. 
장르별로 순회하면서 같은 장르의 것을 가져오고, 재생횟수로 정렬하여 2개만 고유번호를 가져온다. 

순회하면서 장르

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