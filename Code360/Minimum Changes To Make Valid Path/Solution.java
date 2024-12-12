import java.util.LinkedList;
import java.util.HashMap;
import java.util.Deque;

class Pair<K, V> {

    private K key;

    public K getKey() {
        return key;
    }

    private V value;

    public V getValue() {
        return value;
    }

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }
    
    @Override
    public String toString() {
        return key + "=" + value;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 31 * hash + (key != null ? key.hashCode() : 0);
        hash = 31 * hash + (value != null ? value.hashCode() : 0);
        return hash;
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o instanceof Pair) {
            @SuppressWarnings("rawtypes")
            Pair pair = (Pair) o;
            if (key != null ? !key.equals(pair.key) : pair.key != null)
                return false;
            if (value != null ? !value.equals(pair.value) : pair.value != null)
                return false;
            return true;
        }
        return false;
    }
}

public class Solution {
    public static boolean isValid(int x, int y, int n, int m, HashMap<Integer, Integer> visited) {
        if (x < 0 || y < 0 || x >= n || y >= m && visited.containsKey(x * m + y)) {
            return false;
        }

        return true;
    }

    public static int minChanges(int n, int m, char[][] matrix) {
        Deque<Pair<Integer, Integer>> pq = new LinkedList<>();
        HashMap<Integer, Integer> visited = new HashMap<Integer, Integer>();

        pq.addFirst(new Pair<Integer, Integer>(0, 0));
        int[] dirx = new int[4];
        dirx[0] = 1;
        dirx[1] = -1;
        dirx[2] = 0;
        dirx[3] = 0;

        int[] diry = new int[4];
        diry[0] = 0;
        diry[1] = 0;
        diry[2] = 1;
        diry[3] = -1;

        int ans = 0;

        while (pq.size() > 0) {
            int pos = pq.peekFirst().getKey();
            int steps = pq.peekFirst().getValue();
            pq.removeFirst();

            // If already visited then move to next.
            if (visited.containsKey(pos)) {
                continue;
            }

            visited.put(pos, 1);
            int x = pos / m;
            int y = pos % m;

            if (x == n - 1 && y == m - 1) {
                ans = steps;
                break;
            }

            int x1 = x;
            int y1 = y;
            if (matrix[x][y] == 'U') {
                x1--;
            } else if (matrix[x][y] == 'D') {
                x1++;
            } else if (matrix[x][y] == 'R') {
                y1++;
            } else {
                y1--;
            }

            for (int i = 0; i < 4; i++) {
                int xn = x + dirx[i];
                int yn = y + diry[i];
                if (!isValid(xn, yn, n, m, visited)) {
                    continue;
                }

                if (x1 == xn && y1 == yn) {
                    int pos1 = xn * m + yn;
                    pq.addFirst(new Pair<Integer, Integer>(pos1, steps));
                } else {
                    int pos1 = xn * m + yn;
                    pq.addLast(new Pair<Integer, Integer>(pos1, steps + 1));
                }
            }
        }
        return ans;
    }
}