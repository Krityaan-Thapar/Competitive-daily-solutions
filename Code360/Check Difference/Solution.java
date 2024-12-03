import java.util.*;

public class Solution {
	public static boolean checkDiff(int[] arr, int N, int k) {
		HashSet<Integer> seen = new HashSet<Integer>();
		for (int i = 0; i < arr.length; i++) {
			if (seen.contains(arr[i] - k) || seen.contains(arr[i] + k)) {
				return true;
			}
			seen.add(arr[i]);
		}
		return false;
	}
}