import java.util.*;

public class Solution {
	public static int palinCount(String str) {
		int res = 0;
		int n = str.length();
		for (int i = 0; i < n; ++i) {
			int mask = 0;
			for (int j = i; j < n; ++j) {
				int temp = 1 << str.charAt(j) - 'a';
				mask ^= temp;
				if ((mask & (mask - 1)) == 0) {
					++res;
				}
			}
		}
		return res;
	}

	public static int palinCount2(String str) {
		int res = 0;
		int n = str.length();
		Map<Integer, Integer> mp = new HashMap<Integer, Integer>();
		mp.put(0, 1);
		int temp = 0;

		for (int i = 0; i < n; ++i) {
			temp ^= 1 << (str.charAt(i) - 'a');
			int val = mp.containsKey(temp) ? mp.get(temp) : 0;
			res += val;

			for (int j = 0; j < 26; ++j) {
				val = mp.containsKey(temp ^ (1 << j)) ? mp.get(temp ^ (1 << j)) : 0;
				res += val;
			}

			int key = temp;
			int cnt = mp.containsKey(key) ? mp.get(key) : 0;
			mp.put(key, cnt + 1);
		}
		return res;
	}
}
