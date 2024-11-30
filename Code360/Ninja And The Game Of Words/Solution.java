import java.util.*;

public class Solution {
	public static ArrayList<Integer> getFrequency(String str, ArrayList<String> words, int n) {
		String[] bleh = str.split(" ");
		HashMap<String, Integer> m = new HashMap<String, Integer>();

		for (String s : bleh) {
			m.put(s, m.getOrDefault(s, 0) + 1);
		}

		ArrayList<Integer> ans = new ArrayList<>();
		for (String w : words) {
			ans.add(m.getOrDefault(w, 0));
		}
		return ans;
	}
}