import java.util.ArrayList;

public class Solution {
	public static void solve(ArrayList<Integer> digits, int product) {
		int carry = 0;

		for (int i = 0; i < digits.size(); i++) {
			int tmp = product * digits.get(i) + carry;
			digits.set(i, tmp % 10);
			carry = tmp / 10;
		}

		while (carry > 0) {
			digits.add(carry % 10);
			carry /= 10;
		}
	}
	public static void factorial(int n) {
		ArrayList<Integer> digits = new ArrayList<Integer>();
		digits.add(1);

		for (int i = 2; i < n + 1; i++) {
			solve(digits, i);
		}

		for (int i = digits.size() - 1; i >= 0; i--) {
			System.out.print(digits.get(i));
		}
	}
}
