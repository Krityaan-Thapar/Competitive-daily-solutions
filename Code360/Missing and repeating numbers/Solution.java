import java.util.ArrayList;

public class Solution {
    public static int[] missingAndRepeating(ArrayList<Integer> arr, int n) {
        int[] ans = new int[2];
        for (int i : arr) {
            int x = Math.abs(i) - 1;
            if (arr.get(x) < 0) {
                ans[1] = x + 1;
                continue;
            }
            arr.set(x, arr.get(x) * -1);
        }
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > 0 && i + 1 != ans[1]) {
                ans[0] = i + 1;
            }
        }
        return ans;
    }
}