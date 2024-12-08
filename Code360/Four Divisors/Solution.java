import java.util.*;

public class Solution {
	public static int sumFourDivisors(ArrayList<Integer> arr, int n) {
		int ans = 0;
		for (int i : arr) {
			int sum = 0;
			int count = 0;
			int x = 1;

			while (x * x <= i) {
				if (i % x == 0) {
					if (x * x == i) {
						count += 1;
						sum += x;
					} else {
						count += 2;
						sum += x;
						sum += (i / x);
					}
				}
				x++;
			}
			if (count == 4) {
				ans += sum;
			}
		}
		return ans;
	}
}