/*
    Time Complexity     :   O(N ^ 2)
        Space Complexity    :   O(N)

            Where 'N' is the number of types of boxes.
            */

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Arrays;

public class Solution {
	public static int findMaxHeight(ArrayList<Integer> height, ArrayList<Integer> width, ArrayList<Integer> length,
			int n) {
		int[][] boxes = new int[3 * n][3];

		for (int i = 0; i < n; i++) {
			boxes[3 * i][0] = height.get(i);
			boxes[3 * i + 1][0] = width.get(i);
			boxes[3 * i + 2][0] = length.get(i);

			boxes[3 * i][1] = Math.min(width.get(i), length.get(i));
			boxes[3 * i + 1][1] = Math.min(height.get(i), length.get(i));
			boxes[3 * i + 2][1] = Math.min(height.get(i), width.get(i));

			boxes[3 * i][2] = Math.max(width.get(i), length.get(i));
			boxes[3 * i + 1][2] = Math.max(height.get(i), length.get(i));
			boxes[3 * i + 2][2] = Math.max(height.get(i), width.get(i));
		}

		Arrays.sort(boxes, new Comparator<int[]>() {
			public int compare(final int[] box1, final int[] box2) {
				if (box1[1] * box1[2] < box2[1] * box2[2])
					return 1;
				else
					return -1;
			}
		});

		int[] maxHeight = new int[3 * n];
		int result = 0;
		for (int i = 0; i < 3 * n; i++) {
			maxHeight[i] = boxes[i][0];
			for (int j = 0; j < i; j++) {
				if (boxes[j][1] > boxes[i][1] && boxes[j][2] > boxes[i][2]) {
					maxHeight[i] = Math.max(maxHeight[i], boxes[i][0] + maxHeight[j]);
				}
			}
			result = Math.max(result, maxHeight[i]);
		}
		return result;
	}
}