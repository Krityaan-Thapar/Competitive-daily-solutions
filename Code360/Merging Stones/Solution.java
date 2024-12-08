import java.util.ArrayList;

public class Solution {
    public static int mergeStones(int[] stones, int k) {
        if ((stones.length - 1) % (k - 1) != 0) {
            return -1;
        }

        ArrayList<Integer> preArr = new ArrayList<Integer>();
        preArr.add(0);
        for (int pile : stones) {
            preArr.add(preArr.get(preArr.size() - 1) + pile);
        }

        int dp[][] = new int[stones.length][stones.length];
        for (int i = 0; i < stones.length; i++) {
            for (int j = 0; j < stones.length; j++) {
                dp[i][j] = 0;
            }
        }

        for (int start = stones.length - 1; start >= 0; start--) {
            for (int end = start + k - 1; end < stones.length; end++) {
                dp[start][end] = Integer.MAX_VALUE;

                for (int i = start; i < end; i += k - 1) {
                    int firstPile = dp[start][i];
                    int otherPiles = dp[i + 1][end];
                    int mergeCost;

                    if ((end - start) % (k - 1) != 0) {
                        mergeCost = 0;
                    } else {
                        mergeCost = (int) preArr.get(end + 1) - (int) preArr.get(start);
                    }

                    dp[start][end] = Math.min(dp[start][end], firstPile + otherPiles + mergeCost);
                }
            }
        }
        return dp[0][stones.length - 1];
    }
}