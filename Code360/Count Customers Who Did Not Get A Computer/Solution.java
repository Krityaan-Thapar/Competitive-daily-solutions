import java.util.ArrayList;

public class Solution {
	public static int countCustomers(ArrayList<Integer> arr, int k) {
		int[] status = new int[100001];
		int ans = 0;
		for (int i : arr) {
			if (status[i] == 0) {
				if (k > 0) {
					k--;
					status[i] = 1;
				} else {
					ans++;
					status[i] = -1;
				}
			} else if (status[i] == 1) {
				k++;
				status[i] = -1;
			}
		}

		return ans;
	}
}