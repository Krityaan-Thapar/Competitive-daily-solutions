public class Solution {
    static int solver(String A, String B, String C, int[][][] dp, int x, int y, int z, int MOD) {
        if (z == 0) {
            return 1;
        }
        if ((x <= 0 && y <= 0)) {
            return 0;
        }

        if (dp[x][y][z] != -1) {
            return dp[x][y][z];
        }

        int ways = 0;
        for (int i = x - 1; i >= 0; i--) {
            if (A.charAt(i) == C.charAt(z - 1)) {
                ways = (ways + solver(A, B, C, dp, i, y, z - 1, MOD)) % MOD;
            }
        }

        for (int i = y - 1; i >= 0; i--) {
            if (B.charAt(i) == C.charAt(z - 1)) {
                ways = (ways + solver(A, B, C, dp, x, i, z - 1, MOD)) % MOD;
            }
        }
        return dp[x][y][z] = ways;
    }

    public static int countWays(String A, String B, String C) {
        int MOD = 1000000007;
        int[][][] dp = new int[105][105][105];
        for (int i = 0; i < 105; i++) {
            for (int j = 0; j < 105; j++) {
                for (int k = 0; k < 105; k++) {
                    dp[i][j][k] = -1;
                }
            }
        }
        return solver(A, B, C, dp, A.length(), B.length(), C.length(), MOD);
    }
}