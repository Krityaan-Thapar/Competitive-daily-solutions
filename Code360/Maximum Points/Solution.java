public class Solution {
    public static int maximumPoints(int n, int[][] grid) {
        int r = grid.length, c = grid[0].length;
        int ans = 0;
        
        for (int i = 0; i < r; i++) {
            ans += grid[i][i];
            ans += grid[i][c - i - 1];

            if (c - i - 1 == i) {
                ans -= grid[i][i];
            }
        }

        return ans;
    }
}