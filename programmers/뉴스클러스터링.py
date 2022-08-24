'''
자카드유사도 : 교집합 크기를 합집합 크기로 나눈 값
2글자씩 끊어서 소문자로 이뤄진 경우에만 원소로 쓴다.

모두 공집합이면 1

같은 값이어도 중복을 제거해선 아니됨 -> set사용 불가
리스트의 in은 오래 걸릴테니 hash 이용해서 처리해보자
-> collections의 카운터 사용하여 합집합 교집합 연산까지 가능

'''
from collections import Counter
def solution(str1, str2):
    
    # 1칸씩 슬라이딩 하면서 둘다 알파벳인 경우만 추출해 소문자로 저장
    counter_1 = Counter([str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()])
    counter_2 = Counter([str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()])
    
    # 교집합 개수, 합집합 개수 구함
    inter = sum((counter_1 & counter_2).values())
    union = sum((counter_1 | counter_2).values())
    
    # 둘다 공집합이면 65536을, 그렇지 않으면 자카드 유사도에 65536을 곱해 나머지는 버린 값
    # 65536을 먼저 곱해줘야함에 유의
    answer = 65536 if (inter + union == 0) else 65536 * inter // union
    
    return answer