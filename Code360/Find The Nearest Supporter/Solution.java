import java.util.* ;

public class Solution {
    public static List<ArrayList<Integer>> leftRotationsOfArray(List<Integer> nums, List<Integer> queries) {
        int n = nums.size();
        List<ArrayList<Integer>> ans = new ArrayList<ArrayList<Integer>>();

        for (int i : queries) {
            int s_idx = i % n;
            ArrayList<Integer> entry = new ArrayList<>();

            for (int x = 0; x < n; x++) {
                entry.add(nums.get((s_idx + x) % n));
            }
            ans.add(entry);
        }

        return ans;
    }
}