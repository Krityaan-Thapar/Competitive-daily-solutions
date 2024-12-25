import java.util.ArrayList;

public class Solution {
    public static int count_touches(int mask, ArrayList<String> arr, int k, int n, int[] dp) {
        if (mask > 0 && (mask & (mask - 1)) == 0) {
            return 0;
        }

        int ans = (int) 1e9;

        if (dp[mask] != -1) {
            return dp[mask];
        }

        for (int pos = 0; pos < k; pos++) {
            int mask1 = 0;
            int mask2 = 0;
            int cnt = 0;

            for (int i = 0; i < n; i++) {
                if (((1 << i) & mask) != 0) {
                    cnt++;
                    if (arr.get(i).charAt(pos) == '1') {
                        mask2 |= (1 << i);
                    } else {
                        mask1 |= (1 << i);
                    }
                }
            }

            if (mask1 > 0 && mask2 > 0) {
                int a = count_touches(mask1, arr, k, n, dp);
                int b = count_touches(mask2, arr, k, n, dp);
                ans = Math.min(ans, cnt + a + b);
            }
        }
        return dp[mask] = ans;
    }

    public static int minimumTouchesRequired(int n, ArrayList<String> arr) {
        int k = arr.get(0).length();
        int[] dp = new int[1 << n];
        for (int i = 0; i < (1 << n); ++i) {
            dp[i] = -1;
        }
        return count_touches((1 << n) - 1, arr, k, n, dp);
    }
}