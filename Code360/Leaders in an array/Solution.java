import java.util.* ;

public class Solution {
	public static ArrayList<Integer> findLeaders(ArrayList<Integer> elements, int n) {
		Stack<Integer> stk = new Stack<Integer>();
		for(int i = 0; i < elements.size(); i++) {
			int val = elements.get(i);
			while (!stk.isEmpty() && stk.peek() <= val) {
				stk.pop();
			}
			stk.push(val);
		}

		ArrayList<Integer> ans = new ArrayList<Integer>();
		while (!stk.isEmpty()) {
			ans.add(stk.pop());
		}
		Collections.reverse(ans);
		return ans;
	}
}