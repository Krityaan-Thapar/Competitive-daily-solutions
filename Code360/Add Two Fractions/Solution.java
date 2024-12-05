public class Solution {

    public static long[] addFraction(int a, int b, int c, int d) {
        long den = lcm(b, d);
        long num = a * (den / b) + c * (den / d);
        long simpler = gcd(den, num);
        long[] ans = new long[2];
        ans[0] = num / simpler;
        ans[1] = den / simpler;

        return ans;
    }

    public static long gcd(long a, long b) {
        if (a > b) {
            return gcd(b, a);
        }
        
        if (a == 0) {
            return b;
        }
        return gcd(b % a, a);
    }

    public static long lcm(long a, long b) {
        return (a / gcd(a, b)) * b;
    }
}