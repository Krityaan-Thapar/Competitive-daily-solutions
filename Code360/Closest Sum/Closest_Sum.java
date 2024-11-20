import java.util.*;

public class Closest_Sum {
    public static int closest3Sum(ArrayList<Integer> arr, int n, int target) {
        Collections.sort(arr);
        int ans = arr.get(0) + arr.get(1) + arr.get(2);

        for (int i = 0; i < arr.size() - 2; i++) {
            int l = i + 1, r = arr.size() - 1;
            int first = arr.get(i);
            while (l < r) {
                int curr = first + arr.get(l) + arr.get(r);
                if (Math.abs(target - curr) < Math.abs(target - ans)) {
                    ans = curr;
                } else if (curr < ans && (Math.abs(target - curr) == Math.abs(target - ans))) {
                    ans = curr;
                }

                if (curr > target) {
                    r--;
                } else if (curr < target) {
                    l++;
                } else {
                    return target;
                }
            }
        }
        return ans;
    }
}
