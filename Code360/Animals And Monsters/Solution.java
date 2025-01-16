public class Solution {
	static class Point {
		int x;
		int y;

		Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static boolean onLine(Point p, Point q, Point r) {
		if (q.x <= Math.max(p.x, r.x) && q.x >= Math.min(p.x, r.x) && q.y <= Math.max(p.y, r.y)
				&& q.y >= Math.min(p.y, r.y)) {
			return true;
		}
		return false;
	}

	// Function to find the orientation.
	public static int orientation(Point p, Point q, Point r) {
		int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);

		if (val == 0) {
			return 0;
		}
		if (val > 0) {
			return 1;
		}
		return 2;
	}

	public static boolean intersect(Point f1, Point f2, Point a1, Point a2) {
		int o1 = orientation(f1, f2, a1);
		int o2 = orientation(f1, f2, a2);
		int o3 = orientation(a1, a2, f1);
		int o4 = orientation(a1, a2, f2);

		if (o1 != o2 && o3 != o4) {
			return true;
		}

		if (o1 == 0 && onLine(f1, a1, f2)) {
			return true;
		}

		if (o2 == 0 && onLine(f1, a2, f2)) {
			return true;
		}

		if (o3 == 0 && onLine(a1, f1, a2)) {
			return true;
		}

		if (o4 == 0 && onLine(a1, f2, a2)) {
			return true;
		}
		return false;
	}

	public static int isSafe(int n, int[][] points, int x, int y) {
		if (n < 3) {
			return 0;
		}

		Point a1 = new Point(x, y);
		Point a2 = new Point(10000, y);
		int count = 0;

		for (int i = 0; i < n; ++i) {
			Point f1 = new Point(points[i][0], points[i][1]);
			Point f2 = new Point(points[(i + 1) % n][0], points[(i + 1) % n][1]);

			if (intersect(f1, f2, a1, a2)) {
				if (orientation(f1, a1, f2) == 0) {
					return onLine(f1, a1, f2) ? 1 : 0;
				}
				++count;
			}
		}
		return (count % 2);
	}
}