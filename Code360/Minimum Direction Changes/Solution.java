import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.Comparator;

class Node {
	int row, column;
	int distance = (int) 1e6;

	public Node(int r, int c) {
		this.row = r;
		this.column = c;
	}
}

class Edge {
	int destRow, destColumn;
	int weight;
	public Edge(int x, int y, int w) {
		this.destRow = x;
		this.destColumn = y;
		this.weight = w;
	}
}

class TheComparator implements Comparator<Node> {
	public int compare(Node a, Node b) {
		return a.distance - b.distance;
	}
}

public class Solution {
	public static int minDirectionChanges(char[][] grid, int n, int m) {
		Node[][] arr = new Node[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr[i][j] = new Node(i, j);

			}
		}
		@SuppressWarnings("unchecked")
		ArrayList<Edge>[][] adj = new ArrayList[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				adj[i][j] = new ArrayList<>();
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (i + 1 < n) {
					if (grid[i][j] == 'D') {

						adj[i][j].add(new Edge(i + 1, j, 0));
					} else {
						adj[i][j].add(new Edge(i + 1, j, 1));
					}
				}
				if ((j + 1) < m) {
					if (grid[i][j] == 'R') {

						adj[i][j].add(new Edge(i, j + 1, 0));
					} else {
						adj[i][j].add(new Edge(i, j + 1, 1));
					}
				}

				if (i > 0) {
					if (grid[i][j] == 'U') {
						adj[i][j].add(new Edge(i - 1, j, 0));
					} else {
						adj[i][j].add(new Edge(i - 1, j, 1));
					}
				}
				if (j > 0) {
					if (grid[i][j] == 'L') {
						adj[i][j].add(new Edge(i, j - 1, 0));
					} else {
						adj[i][j].add(new Edge(i, j - 1, 1));
					}
				}
			}
		}

		PriorityQueue<Node> pq = new PriorityQueue<>(new TheComparator());
		arr[0][0].distance = 0;
		pq.add(arr[0][0]);

		while (!pq.isEmpty()) {
			Node current = pq.poll();
			for (Edge curr_edge : adj[current.row][current.column]) {
				if ((curr_edge.weight
						+ (arr[current.row][current.column]).distance) < (arr[curr_edge.destRow][curr_edge.destColumn]).distance) {
					arr[curr_edge.destRow][curr_edge.destColumn].distance = curr_edge.weight
							+ (arr[current.row][current.column]).distance;
					pq.add(arr[curr_edge.destRow][curr_edge.destColumn]);
				}
			}
		}
		return (arr[n - 1][m - 1]).distance;
	}
}