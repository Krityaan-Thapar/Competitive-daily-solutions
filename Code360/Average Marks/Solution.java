class Pair{
    char firstLetterOfName;
    int avgMarks;
    Pair(char firstLetterOfName, int avgMarks){
        this.firstLetterOfName = firstLetterOfName;
        this.avgMarks = avgMarks;
    }
}

public class Solution {
	public static Pair averageMarks(char firstLetterOfName, int m1, int m2, int m3) {
		return new Pair(firstLetterOfName, (int) Math.floor((m1 + m2 + m3) / 3));
	}
}