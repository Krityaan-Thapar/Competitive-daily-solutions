public class Solution {
    public static int cubicSquare(int m, int a, String b) {
        long ans = 1;
        long base = a, mod = m;

        int n = b.length();
        for (int i = n - 1; i >= 0; i--) {
            if (b.charAt(i) == '2') {
                ans = (((ans * base) % mod) * base) % mod;
            } else if (b.charAt(i) == '1') {
                ans = (ans * base) % mod;
            }
            base = (((base * base) % mod) * base) % mod;
        }

        return (int) ans;
    }
}