public class Solution {
    public static int maxLength(int n, int[] arr) {
        int ans = 1;

        for (int i = 0; i < n - 1; ++i) {
            int mx = arr[i];
            int mn = arr[i];

            for (int j = i + 1; j < n; ++j) {
                mx = Math.max(mx, arr[j]);
                mn = Math.min(mn, arr[j]);

                if (mx - mn == j - i) {
                    ans = Math.max(ans, mx - mn + 1);
                }
            }
        }
        return ans;
    }
}