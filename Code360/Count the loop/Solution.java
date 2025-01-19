public class Solution {
    public static int countLoop(String p, String q) {
        if (q.charAt(0) == '0') {
            return 0;
        }

        int carry = 0, ans = 0, cur = 0;
        int i = p.length() - 1;
        int j = q.length() - 1;
        
        while (i >= 0 || j >= 0) {
            int p1 = 0;
            if (i >= 0) {
                p1 = p.charAt(i) - '0';
            }

            int q1 = 0;
            if (j >= 0) {
                q1 = q.charAt(j) - '0';
            }

            carry = carry + p1 + q1;
            if (carry == 2) {
                cur += 1;
            } else {
                if (carry <= 1) {
                    cur = 0;
                } else {
                    cur = 1;
                }
            }

            if (carry <= 1) {
                carry = 0;
            } else {
                carry = 1;
            }

            ans = Math.max(ans, cur + 1);
            i -= 1;
            j -= 1;
        }
        return ans;
    }
}