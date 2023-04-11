간# 코딩테스트 연습 > 정렬 > K번째수

- [Link to Problem](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

## Solution1
순회하면서 배열을 slice해서 정렬한 뒤, k번째 수를 반환한다.

```java
// 구현함...
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i += 1) {
            int[] command = commands[i];

            int[] arr = new int[command[1] - command[0] + 1]; // 5 - 2 + 1 = 4
            for (int j = 0; j < arr.length; j += 1) {  //
                arr[j] = array[j + command[0] - 1];
            }

            sort(arr, 0, arr.length - 1);
            answer[i] = arr[command[2] - 1];
        }

        return answer;
    }

    private void sort(int[] arr, int l, int r) {
        if (l < r) {
            int m = (l + r - 1) / 2;

            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    private void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        int[] arrL = new int[n1];
        int[] arrR = new int[n2];

        for (int i = 0; i < n1; i += 1) {
            arrL[i] = arr[l + i];
        }
        for (int i = 0; i < n2; i += 1) {
            arrR[i] = arr[m + 1 + i];
        }

        int i = 0;
        int j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (arrL[i] < arrR[j]) {
                arr[k++] = arrL[i++];
            } else {
                arr[k++] = arrR[j++];
            }
        }

        while (i < n1) {
            arr[k++] = arrL[i++];
        }

        while (j < n2) {
            arr[k++] = arrR[j++];
        }
    }
}
```

## Solution2
API 사용 
```java
import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }
}
```

## 시간복잡도와 공간복잡도
- 시간복잡도: O(nlogn)
- 공간복잡도: O(n)

## 참고 자료

### Merge Sort
