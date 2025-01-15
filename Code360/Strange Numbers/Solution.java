import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public static boolean isStrangeNumber(int currNumber) {
        int rotatedNumber = 0;
        int dummy = currNumber;

        while (dummy > 0) {
            int currDigit = dummy % 10;
            dummy = dummy / 10;

            if (currDigit == 6) {
                currDigit = 9;
            } else if (currDigit == 9) {
                currDigit = 6;
            }
            rotatedNumber = rotatedNumber * 10 + currDigit;
        }

        if (currNumber != rotatedNumber) {
            return true;
        } else {
            return false;
        }
    }

    public static int strangeNumbers(int n) {
        int cntStrange = 0;
        int currNumber;
        Queue<Integer> que = new LinkedList<>();

        ArrayList<Integer> digits = new ArrayList<>();
        digits.add(0);
        digits.add(1);
        digits.add(6);
        digits.add(8);
        digits.add(9);

        for (int i = 0; i < digits.size(); i++) {
            if (digits.get(i) >= 1 && digits.get(i) <= n) {
                que.add(digits.get(i));
            }
        }

        while (que.isEmpty() == false) {
            currNumber = que.peek();
            que.poll();

            if (isStrangeNumber(currNumber)) {
                cntStrange = cntStrange + 1;
            }

            for (int i = 0; i < digits.size(); i++) {
                int appendedNumber = currNumber * 10 + digits.get(i);
                
                if (appendedNumber >= 1 && appendedNumber <= n) {
                    que.add(appendedNumber);
                }
            }
        }
        return cntStrange;
    }
}