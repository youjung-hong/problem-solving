간# 코딩테스트 연습 > 완전탐색 > 최소직사각형

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/86491)

## Solution
순회하면서 가로, 세로 중 큰 값을 가로, 작은 값을 세로로 하여 최대 가로, 세로를 구한다.

```java
class Solution {
    public int solution(int[][] sizes) {
        int w = 0;
        int h = 0;

        for (int i = 0; i < sizes.length; i++) {
            int width, height;
            if (sizes[i][0] > sizes[i][1]) {
                width = sizes[i][0];
                height = sizes[i][1];
            } else {
                width = sizes[i][1];
                height = sizes[i][0];
            }

            w = Math.max(width, w);
            h = Math.max(height, h);
        }

        return w * h;
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: O(n)
- 공간복잡도: O(1)

## 참고 자료

