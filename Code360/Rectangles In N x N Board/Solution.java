public class Solution {
	public static int countRectangles(int n) {
		long MOD = 1000000007;
		long rect = ((((long) n * (long) (n + 1)) % MOD) / 2);
		rect = (rect % MOD * rect % MOD) % MOD;

		long sqr = ((long) n * (long) (n + 1) * (long) (2L * n + 1)) / 6;
		sqr %= MOD;
		long ans = (rect - sqr + MOD) % MOD;
		return (int) (ans % MOD);
	}
}