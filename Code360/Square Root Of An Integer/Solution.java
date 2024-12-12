public class Solution {
    public static int squareRoot(int a) {
        int lo = 0;
        int hi = a;
        int ans = 0;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (mid * mid > a) {
                hi = mid - 1;
            } else {
                ans = mid;
                lo = mid + 1;
            }
        } 
        return ans;
    }
}
