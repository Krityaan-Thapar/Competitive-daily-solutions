import java.util.Queue;
import java.util.LinkedList;

class Coordinates {
    int rowNumber;
    int columnNumber;
    public Coordinates(int cellNumber, int n) {
        this.rowNumber = (cellNumber - 1) / n;
        this.columnNumber = (cellNumber - 1) % n;

        if (this.rowNumber % 2 == 1) {
            this.columnNumber = (n - 1) - this.columnNumber;
        }
        this.rowNumber = (n - 1) - this.rowNumber;
    }
}

public class Solution {
    public static int minDiceThrowToLastCell(int[][] board) {
        int n = board.length;
        int[] minDiceThrow = new int[(n * n) + 1];
        int i;
        for (i = 1; i <= n * n; i++) {
            minDiceThrow[i] = Integer.MAX_VALUE;
        }

        Queue<Integer> Q = new LinkedList<>();
        minDiceThrow[1] = 0;
        Q.add(1);
        while (!Q.isEmpty()) {
            int curCellNumber = Q.poll();
            for (i = 1; i <= 6 && curCellNumber + i <= n * n; i++) {
                int nextCellNumber = i + curCellNumber;
                Coordinates nextCell = new Coordinates(nextCellNumber, n);
                if (board[nextCell.rowNumber][nextCell.columnNumber] != -1) {
                    nextCellNumber = board[nextCell.rowNumber][nextCell.columnNumber];
                }

                if (minDiceThrow[nextCellNumber] > minDiceThrow[curCellNumber] + 1) {
                    minDiceThrow[nextCellNumber] = minDiceThrow[curCellNumber] + 1;
                    Q.add(nextCellNumber);
                }
            }
        }

        int finalMinDiceThrowToLastCell = minDiceThrow[n * n];
        if (finalMinDiceThrowToLastCell == Integer.MAX_VALUE) {
            finalMinDiceThrowToLastCell = -1;
        }
        return finalMinDiceThrowToLastCell;
    }
}