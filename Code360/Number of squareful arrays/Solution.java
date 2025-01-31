import java.util.Arrays;
import java.util.ArrayList;

public class Solution {
    public static boolean isSquare(int x) {
        int t = (int) Math.sqrt(x);
        return (t * t == x);
    }

    public static int fact(int x) {
        int t = 1;
        for (int i = 2; i <= x; i++) {
            t *= i;
        }

        return t;
    }

    public static int numberOfSquarefulArrays(int[] arr, int n) {
        Arrays.sort(arr);
        ArrayList<Integer> s = new ArrayList<>();
        int cnt = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] != arr[i - 1]) {
                s.add(cnt);
                cnt = 0;
            }

            cnt++;
        }

        s.add(cnt);
        int[][] f = new int[1 << n][n];
        for (int i = 0; i < n; i++) {
            f[1 << i][i] = 1;
        }

        for (int k = 1; k < (1 << n); k++) {
            for (int i = 0; i < n; i++) {
                if ((k & (1 << i)) != 0) {
                    for (int j = 0; j < n; j++) {
                        if ((k & (1 << j)) == 0 && isSquare(arr[i] + arr[j])) {
                            f[k | (1 << j)][j] += f[k][i];
                        }
                    }
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += f[(1 << n) - 1][i];
        }
        for (int i = 0; i < s.size(); i++) {
            ans /= fact(s.get(i));
        }
        
        return ans;
    }
}