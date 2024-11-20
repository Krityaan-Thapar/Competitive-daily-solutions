import java.util.ArrayList;
import java.util.Arrays;

public class Minimum_Costs_Of_Subsets {
	public static int minimumCostsubsets(ArrayList<Integer> a, int n, int k) {
		int groupSize = n / k;

		if (groupSize == 1) {
			return 0;
		}

		int[][] dp = new int[1 << n][n];
		for (int i = 0; i < (1 << n); i++) {
			Arrays.fill(dp[i], 1000000000);

		}

		int[] arr = new int[n];

		for (int i = 0; i < n; i++) {
			arr[i] = a.get(i);
		}

		// base cases
		for (int i = 0; i < n; i++) {
			dp[1 << i][i] = -arr[i];
		}

		for (int mask = 0; mask < (1 << n); mask++) {
			int setBits = __builtin_popcount(mask);
			for (int current = 0; current < n; current++) {
				for (int next = 0; next < n; next++) {
					if (setBits % groupSize == 0) {
						int d = mask & (1 << current);
						if (d > 0 && (mask & (1 << next)) == 0) {
							int new_mask = (mask | (1 << next));
							dp[new_mask][next] = Math.min(dp[new_mask][next], dp[mask][current] - arr[next]);

						}
					}

					if (setBits % groupSize == groupSize - 1) {

						int d = (mask & (1 << next));
						int d1 = (mask & (1 << current));
						// always choose greater element to end or increase the size of the group
						if (d1 > 0 && d == 0 && arr[next] > arr[current]) {
							int new_mask = (mask | (1 << next));
							dp[new_mask][next] = Math.min(dp[new_mask][next], dp[mask][current] + arr[next]);
						}
					}

					if (setBits % groupSize > 0 && setBits % groupSize < groupSize - 1) {
						int d = (mask & (1 << next));
						int d1 = (mask & (1 << current));

						if (d1 > 0 && d == 0 && arr[next] > arr[current]) {
							int new_mask = (mask | (1 << next));
							dp[new_mask][next] = Math.min(dp[new_mask][next], dp[mask][current]);
						}
					}
				}
			}
		}

		int ans = 1000000000;

		for (int i = 0; i < n; i++) {
			ans = Math.min(ans, dp[(1 << n) - 1][i]);
		}

		if (ans == 1000000000) {
			ans = -1;
		}

		return ans; // write your code here
	}

	private static int __builtin_popcount(int mask) {

		int cnt = 0;
		while (mask > 0) {
			cnt++;
			mask = (mask) & (mask - 1);
		}

		return cnt;

	}
}