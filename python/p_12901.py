# https://programmers.co.kr/learn/courses/30/lessons/12901
# 2016년

def solution(a, b):
    day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    date = ("FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU")
    time = 0
    
    for i in range(1, a):
        time = time + day[i]
    time = time + b - 1

    return date[time % 7]