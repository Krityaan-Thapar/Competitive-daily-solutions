public class Solution {
	private static boolean bipartiteMatch(int u, boolean[] visited, int[] assign, int[][] mat, int n) {
		for (int v = 0; v < n; v++) {
			if (mat[u][v] == 1 && !visited[v]) {
				visited[v] = true;
				if (assign[v] < 0 || bipartiteMatch(assign[v], visited, assign, mat, n)) {
					assign[v] = u;
					return true;
				}
			}
		}
		return false;
	}

	public static int maxMatch(int[][] mat) {
		int m = mat.length;
		int n = mat[0].length;
		int[] assign = new int[n];

		for (int i = 0; i < n; i++) {
			assign[i] = -1;
		}

		int jobCount = 0;
		for (int u = 0; u < m; u++) {
			boolean[] visited = new boolean[n];

			for (int i = 0; i < n; i++) {
				visited[i] = false;
			}

			if (bipartiteMatch(u, visited, assign, mat, n)) {
				jobCount++;
			}
		}
		return jobCount;
	}
}