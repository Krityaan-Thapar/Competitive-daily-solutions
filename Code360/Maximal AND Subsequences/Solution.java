import java.util.ArrayList;

public class Solution {
	private static long MOD = (long) 1e9 + 7;

	private static long binaryExp(long a, long b) {
		a = a % MOD;
		long res = 1;

		while (b > 0) {
			if ((b & 1) != 0) {
				res = (res * a) % MOD;
			}
			a = (a * a) % MOD;
			b = b >> 1;
		}
		return (int) res;
	}

	private static long factorial(long n) {
		long ans = 1;
		for (int i = 1; i <= n; i++) {
			ans = (ans * i) % MOD;
		}
		return (int) ans;
	}

	public static ArrayList<Integer> maximalANDSubsequences(ArrayList<Integer> arr, long k) {
		ArrayList<Integer> temp = new ArrayList<Integer>(arr);
		for (int i = 30; i >= 0; --i) {
			ArrayList<Integer> setTemp = new ArrayList<Integer>();

			long n = temp.size();
			for (int j = 0; j < n; j++) {
				if ((temp.get(j) & ((int) 1 << i)) != 0) {
					setTemp.add(temp.get(j));
				}
			}

			if (setTemp.size() >= k) {
				temp = setTemp;
			}
		}
		long maxVal = temp.get(0);

		for (int i = 1; i < k; i++) {
			maxVal = (maxVal & temp.get(i));
		}
		long m = temp.size();
		long mFact = factorial(m);
		long mMinusKFact = factorial((m - k));
		long kFact = factorial(k);
		long inverseOfmMinusKFact = binaryExp(mMinusKFact, MOD - 2);
		long inverseOfkFact = binaryExp(kFact, MOD - 2);
		long count = (mFact * inverseOfmMinusKFact) % MOD;
		count = (count * inverseOfkFact) % MOD;
		ArrayList<Integer> ans = new ArrayList<Integer>();
		ans.add((int) maxVal);
		ans.add((int) count);

		return ans;
	}
}