import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
	public static ArrayList<String> nonOverlappingSubstrings(String str) {
		int n = str.length();
		int[] first = new int[26];
		int[] last = new int[26];
		Arrays.fill(first, n);
		Arrays.fill(last, -1);

		for (int i = 0; i < n; i++) {
			first[str.charAt(i) - 'a'] = Math.min(first[str.charAt(i) - 'a'], i);
			last[str.charAt(i) - 'a'] = Math.max(last[str.charAt(i) - 'a'], i);
		}

		int[] valid = new int[n];
		Arrays.fill(valid, -1);

		for (int i = 0; i < n; i++) {
			if (last[str.charAt(i) - 'a'] == -1) {
				continue;
			}
			if (first[str.charAt(i) - 'a'] != i) {
				continue;
			}

			int lastPos = i;
			int pos = last[str.charAt(lastPos) - 'a'];
			while (true) {
				if (lastPos == pos) {
					valid[i] = pos;
					break;
				}
				lastPos++;
				if (first[str.charAt(lastPos) - 'a'] < i) {
					break;
				}
				pos = Math.max(pos, last[str.charAt(lastPos) - 'a']);
			}
		}

		ArrayList<String> ans = new ArrayList<>();
		int start = 0;
		while (true) {
			int pos = Integer.MAX_VALUE;
			int lastPos = -1;
			for (int i = start; i <= Math.min(pos, n - 1); i++) {
				if (valid[i] != -1 && valid[i] <= pos) {
					pos = valid[i];
					lastPos = i;
				}
			}
			if (lastPos == -1) {
				break;
			}
			ans.add(str.substring(lastPos, valid[lastPos] + 1));
			start = pos + 1;
		}
		return ans;
	}
}