import math
def solution(w,h):
    #정사각형일때
    if w == h:
        return w * (w - 1)
    #넓이나 높이가 1이라면 모두 잘리게 됨
    if w == 1 or h == 1:
        return 0
    
    gcd = math.gcd(w, h)
    a = w // gcd
    b = h // gcd
    #최대공약수가 1보다 크면
    if gcd > 1:
        # a x b의 형태의 직사각형이 gcd만큼 생긴 것
        lose = a + b - 1
        return w * h - gcd * lose
    else:
        return w * h - (w + h - 1)

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.4MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.3MB)
"""

# 그런데 사실 모두 같은 식임

import math
def solution(w,h):
    gcd = math.gcd(w, h)
    a, b = w // gcd, h // gcd
    return w * h - gcd * (a + b - 1)

"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.1MB)
"""