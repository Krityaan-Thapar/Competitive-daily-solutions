import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;

class cmp implements Comparator<ArrayList<Integer>> {

    public int compare(ArrayList<Integer> a, ArrayList<Integer> b) {
        return a.get(0) - b.get(0);
    }
}

public class Solution {
    public static int internshipExp(int d, int k, int n, ArrayList<Integer> minExp, ArrayList<Integer> expGained) {
        int currExp = d;
        ArrayList<ArrayList<Integer>> companies = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            companies.add(new ArrayList<>(Arrays.asList(minExp.get(i), expGained.get(i))));
        }

        Collections.sort(companies, new cmp());
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int i = 0;

        while (i < n && k > 0) {
            if (companies.get(i).get(0) <= currExp) {
                maxHeap.add(companies.get(i).get(1));
                i = i + 1;
            } else {
                if (maxHeap.isEmpty() == true) {
                    break;
                }
                currExp = currExp + maxHeap.peek();
                maxHeap.poll();
                k = k - 1;
            }
        }

        while (maxHeap.isEmpty() == false && k > 0) {
            currExp = currExp + maxHeap.peek();
            maxHeap.poll();
            k = k - 1;
        }

        return currExp;
    }
}