import java.util.*;

class fenwickTree {
    int tree[];

    public fenwickTree(int n) {
        tree = new int[n];
    }

    public void insert(int index, int val) {
        while (index < tree.length) {
            tree[index] += val;
            index += index & (-index);
        }
    }
    
    public int sum(int i) {
        int ans = 0;
        while (i > 0) {
            ans += tree[i];
            i -= (i & -i);
        }
        return ans;
    }

    public void clear() {
        for (int i = 0; i < tree.length; i++) {
            tree[i] = 0;
        }
    }
}

public class Solution {
    public static int[][] nestedRangesCount(int[][] ranges, int n) {
        int[][] result = new int[2][n];
        int[] result1 = new int[n];
        int[] result2 = new int[n];
        int arr[][] = new int[n][3];
        fenwickTree os = new fenwickTree(1000001);
        for (int i = 0; i < n; i++) {
            arr[i][0] = ranges[i][0];
            arr[i][1] = ranges[i][1];
            arr[i][2] = i;
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] a1, int[] a2) {
                if (a1[0] == a2[0]) {
                    if (a1[1] < a2[1])
                        return 1;
                    else if (a1[1] > a2[1])
                        return -1;
                    else
                        return 0;
                }

                if (a1[0] > a2[0])
                    return 1;
                else if (a1[0] < a2[0])
                    return -1;
                else
                    return 0;
            }
        });

        for (int i = n - 1; i >= 0; i--) {
            int containedRangesCount = os.sum(arr[i][1]);
            result1[arr[i][2]] = containedRangesCount;
            os.insert(arr[i][1], 1);
        }

        os.clear();

        for (int i = 0; i < n; i++) {
            int containingRangesCount = i - os.sum(arr[i][1] - 1);
            result2[arr[i][2]] = containingRangesCount;
            os.insert(arr[i][1], 1);
            result[0] = result1;
            result[1] = result2;
        }
        return result;
    }
}