# https://programmers.co.kr/learn/courses/30/lessons/12954
# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    num = 0
    
    while len(answer) < n:
        num = num + x
        answer.append(num)
    
    return answer