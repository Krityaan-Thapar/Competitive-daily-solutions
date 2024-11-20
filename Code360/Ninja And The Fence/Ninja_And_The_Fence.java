public class Ninja_And_The_Fence {
    public static int numberOfWays(int n, int k) {
        int answer = k;
        int same = 0, diff = k;

        for (int i = 2; i <= n; i++) {
            same = diff;
            diff = mul(answer, (k - 1));
            answer = add(same, diff);

        }
        return answer;
    }
    public static int add(int a, int b) {
        int mod = (int) 1e9 + 7;
        return (int) (((long) (a % mod) + (b % mod)) % mod);
    }
    public static int mul(int a, int b) {
        int mod = (int) 1e9 + 7;
        return (int) (((long) (a % mod) * (b % mod)) % mod);
    }
}