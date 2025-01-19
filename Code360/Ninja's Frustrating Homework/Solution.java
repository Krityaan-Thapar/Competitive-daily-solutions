import java.util.*;

public class Solution {
    static int MAXS = 500;
    static int MAXC = 26;
    static int[] out;
    static int[] fail;
    static int[][] goTo;

    static int buildMachine(String[] diary, int n) {
        out = new int[MAXS];
        fail = new int[MAXS];
        goTo = new int[MAXS][MAXC + 1];

        for (int i = 0; i < MAXS; i++) {
            Arrays.fill(goTo[i], -1);
        }
        int states = 1;
        for (int i = 0; i < n; i++) {
            String word = diary[i];
            int currentState = 0;
            for (int j = 0; j < word.length(); ++j) {
                int character = word.charAt(j) - 'a';
                if (goTo[currentState][character] == -1) {
                    goTo[currentState][character] = states++;
                }
                currentState = goTo[currentState][character];
            }
            out[currentState] = out[currentState] | (1 << i);
        }

        for (int i = 0; i < MAXC; i++) {
            if (goTo[0][i] == -1) {
                goTo[0][i] = 0;
            }
        }
        Arrays.fill(fail, -1);
        Queue<Integer> q = new LinkedList<Integer>();

        for (int i = 0; i < MAXC; i++) {
            if (goTo[0][i] != 0) {
                fail[goTo[0][i]] = 0;
                q.add(goTo[0][i]);
            }
        }

        while (q.size() > 0) {
            int state = q.poll();

            for (int i = 0; i <= MAXC; i++) {
                if (goTo[state][i] != -1) {
                    int failure = fail[state];
                    while (goTo[failure][i] == -1) {
                        failure = fail[failure];
                    }

                    failure = goTo[failure][i];
                    fail[goTo[state][i]] = failure;
                    out[goTo[state][i]] |= out[failure];
                    q.add(goTo[state][i]);
                }
            }
        }
        return states;
    }

    static int nextState(int currentState, char nextInput) {
        int answer = currentState;
        int character = nextInput - 'a';

        while (goTo[answer][character] == -1) {
            answer = fail[answer];
        }
        return goTo[answer][character];
    }

    public static ArrayList<Integer> searchWords(String booklet, String[] diary) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        buildMachine(diary, diary.length);
        int currentState = 0;

        for (int i = 0; i < booklet.length(); i++) {
            currentState = nextState(currentState, booklet.charAt(i));
            if (out[currentState] == 0) {
                continue;
            }

            for (int j = 0; j < diary.length; j++) {
                if ((out[currentState] & (1 << j)) != 0) {
                    ans.add(i - diary[j].length() + 1);
                }
            }
        }

        Collections.sort(ans);
        return ans;
    }
}
