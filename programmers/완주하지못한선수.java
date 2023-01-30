import java.util.Arrays;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

            Arrays.sort(participant);
            Arrays.sort(completion);

            for (int i = 0; i < completion.length; i++) {
                if (participant[i].compareTo(completion[i]) != 0) {
                    return participant[i];
                }
            }
            return participant[completion.length];
        }
    }
