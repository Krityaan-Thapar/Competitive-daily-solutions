import java.util.ArrayList;

class Anish_and_Queues {
    public static ArrayList<Integer> k_queues(int l, int n, int q, ArrayList<ArrayList<Integer>> queries) {
        int full = l / n;
        ArrayList<Integer> ans = new ArrayList<Integer>();
        ArrayList<Integer> front = new ArrayList<Integer>(n);
        ArrayList<Integer> arr = new ArrayList<Integer>(l);
        ArrayList<Integer> rear = new ArrayList<Integer>(n);

        for (int i = 0; i < n; i++) {
            front.add(-1);
            rear.add(-1);
        }

        for (int i = 0; i < l; i++) {
            arr.add(0);
        }

        for (int i = 0; i < q; i++) {
            int a, b, c = 0;
            if (queries.get(i).size() == 3) {
                a = queries.get(i).get(0);
                b = queries.get(i).get(1);
                c = queries.get(i).get(2);
            } else {
                a = queries.get(i).get(0);
                b = queries.get(i).get(1);

            }
            b -= 1;
            
            if (a == 1) {
                if (rear.get(b) == ((b * full) + (full - 1))) {
                    ans.add(-1);
                } else {
                    if (front.get(b) == -1) {
                        front.set(b, b * full);
                        rear.set(b, b * full);
                    } else {
                        rear.set(b, rear.get(b) + 1);
                    }
                    arr.set(rear.get(b), c);
                    ans.add(0);
                }
            }
            
            else {
                if (front.get(b) == -1) {
                    ans.add(-1);
                } else {
                    ans.add(arr.get(front.get(b)));
                    front.set(b, front.get(b) + 1);
                    if (front.get(b) > rear.get(b)) {
                        front.set(b, -1);
                        rear.set(b, -1);
                    }
                }
            }
        }
        return ans;
    }

}