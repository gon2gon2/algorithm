class Solution {
    public int solution(String s) {
        int answer = 0;
        int startIndex = 0;
        int lastIndex = s.length();
        
        do {
            startIndex = checkAndIncrement(s, startIndex);
            answer += 1;
        } while(startIndex != lastIndex);
        
        return answer;
    }
    
    // input 인덱스부터 하나씩 이동하며 x와 x가 아닌것의 숫자를 +1 하다가 
    // 둘이 같아지거나 해당 문자열 끝에 도달하면 해당 index 리턴
    private int checkAndIncrement(String originalString, int startIndex){
        
        char startChar = originalString.charAt(startIndex);
        int sameCount = 0;
        int diffCount = 0;
        
        // 둘이 같아질때까지 for문 ㄱ
        for (int i = startIndex; i < originalString.length(); i++){
            
            char nowChar = originalString.charAt(i);
            
            if (nowChar == startChar){
                sameCount++;
            } else{
                diffCount++;
            }
            
            if (sameCount == diffCount){
                return i+1;
            }
        }
        
        return originalString.length();
    }
}
