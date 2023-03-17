# 코딩테스트 연습 > 해시 > 전화번호 목록

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=java)

## Solution1
전화번호를 정렬하고, 전화번호를 넣기 전 전화번호의 앞 몇 글자로 시작하는 글자가 있는 지 확인한다. 
있으면 false를 리턴하고 종료, 없으면 전화번호를 해시 테이블에 넣고 다음 걸로 넘어간다. 

```java
import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        // 1. 전화번호를 정렬한다.
        Arrays.sort(phone_book); // O(nlogn)

        
        // 2. 전화번호의 접두어가 존재하는 지 확인한다.
        Set<String> set = new HashSet<>();
        for (String p : phone_book) { // O(n)
            // 2.1 전화번호의 서브스트링이 해시테이블에 존재하는 지 확인한다.
            for (int i = 1; i < p.length(); i++) { // O(n)
                if (set.contains(p.substring(0, i))) // O(1)
                    return false; // 있으면 false
            }
            // 2.2 해시테이블에 추가한다. O(1)
            set.add(p);
        }
        return true;
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: 평균 O(n^2) = O(nlong) + O(n) * (O(n) + O(1))
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


--- 

## Solution2
전화번호를 정렬한다. 
바로 다음 값이 현재 값을 포함하는 지 확인한다. 

```java
import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        // 1. 전화번호를 정렬한다.
        Arrays.sort(phone_book); // O(nlogn)

        // 2. 바로 뒤가 현재 값을 접두어로 갖는 지 확인한다. 
        for (int i = 0; i < phone_book.length; i += 1) { // O(n)
            if (phone_book[i + 1].startsWith(phone_book[i])) { // O(n)
                return false;
            }
        }

        return true;
    }
}
```
## 시간복잡도와 공간복잡도
- 시간복잡도: O(n^2) = O(nlog(n) + O(n) * O(n)) 
- 공간복잡도: O(n)