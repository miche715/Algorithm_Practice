# https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 카드 뭉치

def solution(cards1, cards2, goal):
    while True:
        if len(cards1) > 0 and cards1[0] == goal[0]:
            cards1.pop(0)
            goal.pop(0)
        elif len(cards2) > 0 and cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
        else: return "No"
        
        if len(goal) == 0:
            return "Yes"