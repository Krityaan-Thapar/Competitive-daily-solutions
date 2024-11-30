public class Solution {
	public static String isPossible(String str, int n) {
	    int[] curr = new int[2];
		curr[0] = 0;
		curr[1] = 0;
		
		int[][] d = new int[4][2];
		d[0][0] = 1;
		d[0][1] = 0;
		d[1][0] = 0;
		d[1][1] = 1;
		d[2][0] = -1;
		d[2][1] = 0;
		d[3][0] = 0;
		d[3][1] = -1;
		
		int facing = 0;
		for (int i = 0; i < str.length(); i++) {
			if (str.charAt(i) == 'L') {
				facing = (facing + 3) % 4;
			} else if (str.charAt(i) == 'R') {
				facing = (facing + 1) % 4;
			} else {
				curr[0] += d[facing][0];
				curr[1] += d[facing][1];
			}
		}
		
		if (curr[0] == 0 && curr[1] == 0) {
			return "True";
		}

		if (facing != 0) {
			return "True";
		}
		
		return "False";
	}
}