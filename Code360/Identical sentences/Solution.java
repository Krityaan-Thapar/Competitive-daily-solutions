import java.util.HashMap;
import java.util.ArrayList;

class DisjointSet {
    int count;
    int[] parent;
    int[] rank;

    DisjointSet(int n) {
        count = n;
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) { 
            parent[i] = (i);
            rank[i] = (0);
        }
    }

    int findSet(int v) {
        if (parent[v] == v)
            return v;
        return parent[v] = findSet(parent[v]);
    }

    void unionSets(int a, int b) {
        int pa = findSet(a);
        int pb = findSet(b);
        if (pa != pb) {
            if (rank[pa] < rank[pb]) {
                int x = pa;
                pa = pb;
                pb = x;
            }

            parent[pb] = pa;
            if (rank[pb] == rank[pa])
                rank[pa]++;
            count--;
        }
    }

    int getCount() {
        return count;
    }
};

public class Solution {
    public static boolean identicalSentences(ArrayList<String> word1, ArrayList<String> word2,
        ArrayList<ArrayList<String>> pairs, int n, int m, int p) {

        if (n != m) {
            return false;
        }
        DisjointSet ds = new DisjointSet(2 * p + 1);
        HashMap<String, Integer> words = new HashMap<>();
        int id = 1;

        for (int i = 0; i < p; i++) {
            if (words.get(pairs.get(i).get(0)) == null) {
                words.put(pairs.get(i).get(0), id++);
            }
            if (words.get(pairs.get(i).get(1)) == null) {
                words.put(pairs.get(i).get(1), id++);
            }

            int u = words.get(pairs.get(i).get(0)), v = words.get(pairs.get(i).get(1));
            ds.unionSets(u, v);
        }

        for (int i = 0; i < n; i++) {
            String u = word1.get(i), v = word2.get(i);
            if (u.equals(v) == true) {
                continue;
            }
            
            if (words.get(u) == null || words.get(v) == null || ds.findSet(words.get(u)) != ds.findSet(words.get(v))) {
                return false;
            }
        }
        return true;
    }
}
