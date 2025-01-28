public class Solution {
	public static void print(int n) {
		int parity = 1;
		for (int i = n; i > 0; i--) {
			for (int j = 0; j < i; j++) {
				System.out.print(parity);
			}
			parity = (parity + 1) % 2;
			System.out.println();
		}
	}
}