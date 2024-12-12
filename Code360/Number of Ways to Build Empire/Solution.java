import java.math.*;
import java.util.*;

public class Solution {
    public static int mod = 1000000007;
    public static long binpow(int i, int j, long[] fact) {
        long mod = 1000000007;
        long a = fact[i];
        long b = ((fact[i - j] % mod) * (fact[j] % mod)) % mod;
        BigInteger B = BigInteger.valueOf(b);
        long binverse = B.modInverse(BigInteger.valueOf(mod)).longValue();
        return ((a) * (binverse % mod)) % mod;
    }
    
    public static long[] dfs(int root, List<Integer> graph[], long[] dp) {
        long res[] = new long[] { 1, 0 };
        int cnt = 0;
        List<long[]> list = new ArrayList<>();
        if (graph[root] != null) {
            for (int next : graph[root]) {
                long v[] = dfs(next, graph, dp);
                cnt = cnt + (int) v[0];
                list.add(v);
            }
        }

        res[0] += cnt;
        long com = 1;
        for (long p[] : list) {
            long choose = binpow(cnt, (int) (p[0]), dp);
            cnt -= p[0];
            com = com * choose;
            com %= mod;
            com = com * p[1];
            com %= mod;
        }

        res[1] = com;
        return res;
    }

    public static int waysToBuildEmpire(int n, int[] prevKingdom) {
        @SuppressWarnings("unchecked")
        List<Integer> graph[] = new ArrayList[n + 1];
        long fact[] = new long[prevKingdom.length + 1];

        Arrays.setAll(graph, e -> new ArrayList<>());
        fact[0] = fact[1] = 1;

        for (int i = 2; i < fact.length; i++) {
            fact[i] = fact[i - 1] * i;
            fact[i] %= mod;
        }

        for (int i = 1; i < prevKingdom.length; i++) {
            int pre = prevKingdom[i];
            graph[pre].add(i);
        }
        long res[] = dfs(0, graph, fact);
        return (int) (res[1] % mod);
    }
}