import java.util.ArrayList;

public class Solution {
    public static int getMaxFruits(ArrayList<Integer> basket, int n) {
        ArrayList<ArrayList<Integer>> dp = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < n; i++) {
            dp.add(new ArrayList<Integer>(n));
            for (int j = 0; j < n; j++) {
                dp.get(i).add(0);
            }
        }

        for (int k = 0; k < basket.size(); k++) {
            for (int i = 0, j = k; j < basket.size(); j++, i++) {
                int a, b, c;
                if (i + 2 > j) {
                    a = 0;
                } else {
                    a = dp.get(i + 2).get(j);
                }

                if (i + 1 > j - 1) {
                    b = 0;
                } else {
                    b = dp.get(i + 1).get(j - 1);
                }

                if (i > j - 2) {
                    c = 0;
                } else {
                    c = dp.get(i).get(j - 2);
                }

                dp.get(i).set(j, Math.max(basket.get(i) + Math.min(a, b), basket.get(j) + Math.min(b, c)));
            }
        }
        return dp.get(0).get(n - 1);
    }
}