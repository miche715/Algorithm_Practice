# https://programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값

def solution(s):
    num = list(map(int, s.split(" ")))
    num.sort()
    
    return str(num[0]) + " " + str(num[-1])