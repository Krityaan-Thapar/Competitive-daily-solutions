import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class pair {
    int first;
    int second;

    pair() {
    }

    pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}

public class Solution {
    static int NUM;
    static int timer;
    static int component;
    static int MAXL;
    static int vis;
    static int now;
    static ArrayList<ArrayList<Integer>> graph;
    static int[] U, V, isBridge, componentNo, visited, parent, disc, start, finish, C, S, L;
    static ArrayList<ArrayList<Integer>> Tree;
    static ArrayList<Queue<Integer>> Queue;
    static int[][] P;

    public static int adjacent(int u, int adj) {
        if (U[adj] == u) {
            return V[adj];
        }
        return U[adj];
    }

    public static int dfs0(int u, int p) {
        visited[u] = 1;
        timer++;
        disc[u] = timer;
        int low = timer;

        for (int i = 0; i < graph.get(u).size(); i++) {
            int adj = graph.get(u).get(i);
            int v = adjacent(u, adj);

            if (visited[v] == 0) {
                int mn = dfs0(v, adj);
                low = Math.min(mn, low);
                if (disc[u] < mn) {
                    isBridge[adj] = 1;
                }
            }
            else if (adj != p) {
                low = Math.min(disc[v], low);
            }
        }

        return low;
    }

    public static void dfs1(int s) {
        Queue.get(component).add(s);
        visited[s] = 1;
        int currComponent = component;
        while (!Queue.get(currComponent).isEmpty()) {
            int node = Queue.get(currComponent).poll();
            componentNo[node] = currComponent;
            for (int i = 0; i < graph.get(node).size(); i++) {
                int adj = graph.get(node).get(i);
                int v = adjacent(node, adj);
                if (isBridge[adj] > 0 &&
                        visited[v] == 0) {
                    component++;
                    Tree.get(currComponent).add(component);
                    Tree.get(component).add(currComponent);
                    dfs1(v);
                } else if (visited[v] == 0) {
                    visited[v] = 1;

                    Queue.get(currComponent).add(v);
                }
            }
        }
    }

    public static void dfs2(int u, int p) {
        L[u] = p != -1 ? L[p] + 1 : 1;
        P[0][u] = p;
        start[u] = ++now;

        for (int j = 1; j < MAXL; j++) {
            int x = P[j - 1][u];
            if (x < 0) {
                break;
            }
            P[j][u] = P[j - 1][x];
        }

        ++vis;
        for (int i = 0; i < Tree.get(u).size(); i++) {
            int v = Tree.get(u).get(i);
            if (v == p) {
                continue;
            }
            dfs2(v, u);
        }

        finish[u] = ++now;
        return;
    }

    public static boolean isAncestor(int u, int a) {
        if (u == a) {
            return true;
        }

        if (start[u] < start[a] && finish[u] > finish[a]) {
            return true;
        }

        return false;
    }

    public static int lca(int p, int q) {
        int log, i;

        if (L[p] < L[q]) {
            int temp = p;
            p = q;
            q = temp;
        }
        for (log = 1; (1 << log) <= L[p]; log++)
            ;
        log--;

        for (i = log; i >= 0; i--) {
            if (L[p] - (1 << i) >= L[q]) {
                p = P[i][p];
            }
        }

        if (p == q) {
            return p;
        }

        for (i = log; i >= 0; i--) {

            if (P[i][p] != -1 && P[i][p] != P[i][q]) {
                p = P[i][p];
                q = P[i][q];
            }
        }

        return P[0][p];
    }

    public static pair getCommonPath(int u, int a, int v, int b) {
        if (!isAncestor(v, a)) {
            return new pair(0, 0);
        }

        int x = lca(a, b);
        if (L[v] < L[u]) {
            if (isAncestor(u, x)) {
                return new pair(u, x);
            }
        }
        else {
            if (isAncestor(v, x)) {
                return new pair(v, x);
            }
        }
        return new pair(0, 0);
    }

    public static int getdist(int a, int b, int lca) {
        return L[a] + L[b] - 2 * L[lca];
    }

    public static int getanswer(int a, int b, int c, int d) {
        int u = lca(a, b), v = lca(c, d);
        int ret = getdist(c, d, v);

        pair X;
        X = getCommonPath(u, a, v, c);
        ret -= getdist(X.first, X.second, lca(X.first, X.second));
        X = getCommonPath(u, a, v, d);
        ret -= getdist(X.first, X.second, lca(X.first, X.second));
        X = getCommonPath(u, b, v, c);
        ret -= getdist(X.first, X.second, lca(X.first, X.second));
        X = getCommonPath(u, b, v, d);
        ret -= getdist(X.first, X.second, lca(X.first, X.second));

        return ret;
    }

    public static int[] countBridge(int n, int m, int q, int[][] edges, int[][] queries) {
        NUM = n + 1;
        timer = 0;
        component = 0;
        MAXL = 19;
        vis = 0;
        now = -1;

        graph = new ArrayList<>(NUM);
        U = new int[m];
        V = new int[m];
        isBridge = new int[m];
        Tree = new ArrayList<>(NUM);
        visited = new int[NUM];
        parent = new int[NUM];

        disc = new int[NUM];
        Queue = new ArrayList<>(NUM);
        componentNo = new int[NUM];
        L = new int[NUM];
        P = new int[MAXL][NUM];
        C = new int[NUM];
        S = new int[NUM];
        start = new int[NUM];
        finish = new int[NUM];

        for (int i = 0; i < NUM; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < NUM; i++) {
            Tree.add(new ArrayList<>());
        }

        for (int i = 0; i < NUM; i++) {
            Queue.add(new LinkedList<Integer>());
        }

        for (int i = 0; i < m; i++) {
            int u, v;
            u = edges[i][0];
            v = edges[i][1];
            U[i] = v;
            V[i] = u;
            graph.get(u).add(i);
            graph.get(v).add(i);

        }
        Arrays.fill(visited, 0);
        dfs0(0, -1);

        Arrays.fill(visited, 0);
        dfs1(0);
        dfs2(0, -1);

        int ans[] = new int[q];
        for (int i = 0; i < q; i++) {
            int a, b, c, d;
            a = queries[i][0];
            b = queries[i][1];
            c = queries[i][2];
            d = queries[i][3];
            int temp = getanswer(componentNo[a], componentNo[b], componentNo[c], componentNo[d]);
            ans[i] = temp;
        }
        return ans;
    }
}