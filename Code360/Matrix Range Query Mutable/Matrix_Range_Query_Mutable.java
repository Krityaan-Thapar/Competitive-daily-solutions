import java.util.* ; 
public class Matrix_Range_Query_Mutable {
    public static int[] matrixRangeSum(int[][] grid, int[][] queries)  {
        ArrayList<Integer> ans = new ArrayList<Integer>();

        for (int i = 0; i < queries.length; i++) {
            int[] row = queries[i];
            if (row[0] == 1) {
                int s_r = row[1], s_c = row[2], e_r = row[3], e_c = row[4];
                int sum = 0;
                for (int x = s_r; x <= e_r; x++) {
                    for (int y = s_c; y <= e_c; y++) {
                        sum += grid[x][y];
                    }
                }
                ans.add(sum);
            } else {
                int x = row[1], y = row[2];
                grid[x][y] = row[3];
            }
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}