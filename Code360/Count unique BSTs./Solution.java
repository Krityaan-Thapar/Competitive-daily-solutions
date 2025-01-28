import java.util.*;

public class Solution {
	public static long totalTreesHelper(ArrayList<Long> memo, int num) {
		long mod = 1000000007;
		long sum = 0;

		if (num == 1 || num == 0) {
			return 1;
		}
		if (memo.get(num) != -1) {
			return memo.get(num);
		}

		for (int i = 0; i < num; i++) {
			sum = (sum % mod + (totalTreesHelper(memo, i) % mod * totalTreesHelper(memo, num - i - 1) % mod) % mod)
					% mod;
		}

		memo.set(num, sum);
		return sum;
	}

	public static long totalTrees(int num) {
		ArrayList<Long> memo = new ArrayList<Long>(501);
		for (int i = 0; i <= 500; i++) {
			memo.add(-1L);
		}

		return totalTreesHelper(memo, num);
	}
}