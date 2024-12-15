import java.math.RoundingMode;
import java.text.DecimalFormat;

class Pair {
    double first;
    double second;

    Pair(double x, double y) {
        first = x;
        second = y;
    }
}

public class Solution {
    public static double findDis(double[][] location, Pair point) {
        double sum = 0;

        for (int i = 0; i < location.length; i++) {
            double distx = (location[i][0] - point.first);
            double disty = (location[i][1] - point.second);
            sum += Math.sqrt((distx * distx) + (disty * disty));
        }
        return sum;
    }

    public static double positionForCentre(double[][] location, int N) {
        Pair curPoint = new Pair(0, 0);
        double minDis;

        for (int i = 0; i < N; i++) {
            curPoint.first = curPoint.first + location[i][0];
            curPoint.second = curPoint.second + location[i][1];
        }

        curPoint.first = (double) (curPoint.first) / (N);
        curPoint.second = (double) (curPoint.second) / (N);
        minDis = findDis(location, curPoint);
        int k = 0;

        while (k < N) {
            for (int i = 0; i < N && i != k; i++) {
                Pair newPoint = new Pair(0, 0);
                newPoint.first = location[i][0];
                newPoint.second = location[i][1];
                double dis = findDis(location, newPoint);

                if (dis < minDis) {
                    curPoint = newPoint;
                    minDis = dis;
                }
            }
            k++;
        }
        
        double[][] directions = { { 0.0, 1.0 }, { 0.0, -1.0 }, { 1.0, 0.0 }, { -1.0, 0.0 } };
        double shift = 100000;
        double minShift = 0.00001;

        while (shift > minShift) {
            int flag = 0;
            for (int i = 0; i < 4; i++) {
                Pair newPoint = new Pair(0.0, 0.0);
                newPoint.first = curPoint.first + (double) shift * (directions[i][0]);
                newPoint.second = curPoint.second + (double) shift * (directions[i][1]);
                double dis = findDis(location, newPoint);

                if (dis < minDis) {
                    curPoint = newPoint;
                    minDis = dis;
                    flag = 1;
                    break;
                }
            }

            if (flag == 0)
                shift = shift / 2.00;
        }

        minDis = (minDis * 1000.0) / 1000.0;
        DecimalFormat df_obj = new DecimalFormat("#.###");
        df_obj.setRoundingMode(RoundingMode.CEILING);

        return Double.parseDouble(df_obj.format(minDis));

    }
}
