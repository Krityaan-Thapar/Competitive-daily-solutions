public class Solution {
	public static int minimumKnightMoves(int x, int y) {
		x = Math.abs(x);
		y = Math.abs(y);
		if (x > y) {
			int temp = x;
			x = y;
			y = temp;
		}

		if (x == 0 && y == 1) {
			return 3;
		}
		if (x == 1 && y == 1) {
			return 2;
		}

		if (y >= 2 * x) {
			return (y + 1) / 2 + (y / 2 - x) % 2;
		} else {
			return (y + x) / 3 + (y + x) % 3;
		}
	}
}