public class Solution {
    public static int totalSteps(int n, int k, int[] flowers) {
        int ans = 0;
        int curr = k;
        int idx = 0;
        
        while (idx < n) {
            curr -= flowers[idx];
            if (idx + 1 < n && curr < flowers[idx + 1]) {
                ans += idx + idx + 2;
                curr = k;
            }
            ans++;
            idx++;
        }
        return ans;
    }
}