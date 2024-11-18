import java.util.*;
 
public class Special_Sum {
	public static int specialSum(ArrayList<Integer> arr, int n) {
		ArrayList<Integer> prefix = new ArrayList<Integer>();
		prefix.add(0);
		int curr = 0;
		for (int i: arr) {
			prefix.add(prefix.get(curr++) + i);
		}
		
		ArrayList<Integer> suffix = new ArrayList<Integer>();
		suffix.add(prefix.get(curr));
		curr = 0;
		for (int i: arr) {
			suffix.add(suffix.get(curr++) - i);
		}

		int ans = 50000;
		for (int i = 0; i < n; i++) {
			ans = Math.min(ans, prefix.get(i + 1) + suffix.get(n - i - 1));
		}
		return ans;
	}
}

