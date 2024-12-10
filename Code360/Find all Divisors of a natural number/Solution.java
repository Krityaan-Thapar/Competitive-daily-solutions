import java.util.* ;

public class Solution {
	public static ArrayList<Integer> getAllDivisors(int n){
		int i = 2;
		ArrayList<Integer> ans = new ArrayList<>();
		ans.add(1);
		Stack<Integer> bleh = new Stack<>();

		while (i * i <= n) {
			if (n % i == 0) {
				ans.add(i);
				if (i * i != n) {
					bleh.add(n / i);
				} 
			}
			i += 1;
		}

		while (bleh.size() > 0) {
			ans.add(bleh.pop());
		}
		
		ans.add(n);
		return ans;
	}
}