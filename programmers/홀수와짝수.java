class Solution {
    public String solution(int num) {
        String answer = "";
        
        if (num % 2 == 1 || num % 2 == -1) {
            answer = "Odd";
        } else {
            answer = "Even";
        }
        return answer;
    }
}
// 위는 조건이 2개나 필요
class Solution {
    public String solution(int num) {
        String answer = "";
        
        if (num % 2 == 0) {
            answer = "Even";
        } else {
            answer = "Odd";
        }
        return answer;
    }
}