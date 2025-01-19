public class Solution {
    static int maxn = 1000000;
    static int Bit[] = new int[maxn];

    public static int[] fenwikTree(int[] arr, int N) {
        int res[] = new int[N];
        for (int i = 0; i < maxn; i++) {
            Bit[i] = 0;
        }

        solve(arr, N, res);
        return res;
    }

    private static void solve(int[] arr, int N, int[] res) {
        for (int i = 0; i < N; i++) {
            int index;
            int sum = 0;
            index = 100000;
            while (index > 0) {
                sum = sum + Bit[index];
                index = index - (index & -index);
            }

            int sumNow = 0;
            index = arr[i];
            while (index > 0) {
                sumNow = sumNow + Bit[index];
                index = index - (index & -index);
            }

            int ans = sum - sumNow;
            res[i] = ans;
            index = arr[i];
            while (index <= 100000) {
                Bit[index] = Bit[index] + arr[i];
                index = index + (index & -index);
            }
        }
    }
}