import java.util.HashMap;

public class Solution {
    public static int[] specialSubarray(int n, int[] arr) {
        HashMap<Integer, Integer> left = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> freqMap = new HashMap<Integer, Integer>();
        int maxFreq = 0;
        int minLen = -1;
        int startIdx = -1;

        for (int i = 0; i < n; i++) {
            int x = arr[i];
            if (!freqMap.containsKey(x)) {
                left.put(x, i);
                freqMap.put(x, 1);
            } else {
                freqMap.put(x, freqMap.get(x) + 1);
            }

            if (freqMap.get(x) > maxFreq) {
                maxFreq = freqMap.get(x);
                minLen = i - left.get(x) + 1;
                startIdx = left.get(x);
            } else if ((freqMap.get(x) == maxFreq) && (i - left.get(x) + 1 < minLen)) {
                minLen = i - left.get(x) + 1;
                startIdx = left.get(x);
            }
        }

        int ans[] = new int[minLen];
        int idx = 0;
        for (int i = startIdx; i < startIdx + minLen; i++) {
            ans[idx++] = arr[i];
        }
        return ans;
    }
}