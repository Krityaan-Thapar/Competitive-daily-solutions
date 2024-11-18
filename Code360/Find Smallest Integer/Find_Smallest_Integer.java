 public class Find_Smallest_Integer {
	public static int findSmallestInteger(int[] arr) {
		int ans = 1;
		for (int i = 0; i < arr.length && arr[i] <= ans; i++) {
			ans = ans + arr[i];
		}
		return ans;
	}
}