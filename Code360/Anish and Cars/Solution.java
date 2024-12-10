import java.util.* ;

public class Solution {
    public static int find(int n, int[] position, int[] speed, int d) {
        int ans = 0;
        int[][] cars = new int[n][];
        
        for(int i = 0; i < n; i++){
            cars[i] = new int[]{d - position[i], speed[i]};
        }
        
        Arrays.sort(cars, (a, b) -> Integer.compare(a[0], b[0]));
        float ma = 0;
        for (int i = 0; i < n; i++){
            float t = (float)cars[i][0] / cars[i][1];
            if (t <= ma){
                continue;
            }
            else{
                ans += 1;
                ma = t;
            }
        }
        return ans;
    }
}