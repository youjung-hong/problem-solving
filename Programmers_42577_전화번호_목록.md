# 코딩테스트 연습 > 해시 > 전화번호 목록

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=java)

## Solution
전화번호 목록을 해시테이블에 추가한다. 
이 때, 접두어가 일치하는 것이 있는 지 확인하기 위해 추가할 전화번호 값을 첫번째 단어부터 마지막 단어까지 비교하면서 접두어가 존재하는 지 확인한다. 

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> set = new HashSet<>();
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