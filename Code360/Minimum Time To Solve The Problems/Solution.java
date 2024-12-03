public class Solution {
    public static long minimumRequiredTime(int subjects[], int k) {
        int n = subjects.length;
        long sum = 0;
        long lo = 10000000000L;

        for (int i = 0; i < n; i++) {
            sum += subjects[i];
            if (subjects[i] < lo) {
                lo = subjects[i];
            }
        }

        if (k == 1) {
            return sum;
        }
        if (n == 1) {
            return subjects[0];
        }

        long hi = sum;
        long ans = sum;

        while (lo <= hi) {
            long mid = lo + (hi - lo) / 2;
            if (isGood(subjects, n, k, mid)) {
                hi = mid - 1;
                ans = mid;
            } else {
                lo = mid + 1;
            }
        }

        return ans; 
    }

    public static boolean isGood(int[] subjects, int n, int k, long val) {
        long temp = val;
        int i = 0;
        int count = 1;

        while (i < n) {
            if (count > k) {
                return false;
            }

            if (subjects[i] > temp) {
                count++;
                temp = val;
            } else {
                temp -= subjects[i];
                i++;
            }
        }

        return true;

    }
}