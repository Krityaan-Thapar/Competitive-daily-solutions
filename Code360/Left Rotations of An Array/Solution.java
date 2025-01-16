import java.util.*;

public class Solution {
	public static ArrayList<Integer> prevSmall(ArrayList<Integer> arr, int n) {
		ArrayList<Integer> ans = new ArrayList<>();
		Stack<Integer> q = new Stack<Integer>();

		for (int i = 0; i < arr.size(); i++) {
			while (!q.isEmpty() && q.peek() >= arr.get(i)) {
				q.pop();
			}

			if (q.isEmpty()) {
				ans.add(-1);
			} else {
				ans.add(q.peek());
			}

			q.add(arr.get(i));
		}
		return ans;
	}
}
