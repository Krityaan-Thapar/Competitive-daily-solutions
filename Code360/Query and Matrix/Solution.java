import java.util.*;

public class Solution {
	public static int[] query(int[][] mat, int m, int n, String[] q) {
		int r = mat.length, c = mat[0].length;
		ArrayList<Integer> ans = new ArrayList<Integer>();

		for (int i = 0; i < q.length; i++) {
			if (q[i].charAt(0) == '1') {
				if (q[i].charAt(1) == 'R') {
					int r_num = Character.getNumericValue(q[i].charAt(2)); 
					for (int x = 0; x < c; x++) {
						mat[r_num][x] = (mat[r_num][x] + 1) % 2;
					}
				} else {
					int c_num = Character.getNumericValue(q[i].charAt(2));
					for (int x = 0; x < r; x++) {
						mat[x][c_num] = (mat[x][c_num] + 1) % 2;
					}
				}
			} else {
				if (q[i].charAt(1) == 'R') {
					int r_num = Character.getNumericValue(q[i].charAt(2));
					int c1 = 0;
					for (int x = 0; x < c; x++) {
						if (mat[r_num][x] == 0) {
							c1++;
						}
					}
					ans.add(c1);
				} else {
					int c_num = Character.getNumericValue(q[i].charAt(2));
					int c2 = 0;
					for (int x = 0; x < r; x++) {
						if (mat[x][c_num] == 0) {
							c2++;
						}
					}
					ans.add(c2);
				}
			}
		}

		int[] res = new int[ans.size()];
		for (int i = 0; i < ans.size(); i++) {
			res[i] = ans.get(i);
		}
		return res;
	}
}