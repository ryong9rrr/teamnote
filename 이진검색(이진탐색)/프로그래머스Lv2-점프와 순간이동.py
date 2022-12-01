# 효율성 테스트에서 실패
def solution(n):
    dp = [0] * (n + 1)
    
    for x in range(1, n + 1):
        if x % 2 == 0:
            dp[x] = dp[x // 2]
        else:
            dp[x] = dp[x - 1] + 1
    
    return dp[-1]
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.15ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.19ms, 10.3MB)
테스트 8 〉	통과 (0.15ms, 10.1MB)
테스트 9 〉	통과 (0.20ms, 10MB)
테스트 10 〉	통과 (0.10ms, 10.2MB)
테스트 11 〉	통과 (0.21ms, 10.2MB)
테스트 12 〉	통과 (0.21ms, 10.2MB)
테스트 13 〉	통과 (0.21ms, 10.2MB)
테스트 14 〉	통과 (0.15ms, 10.2MB)
테스트 15 〉	통과 (0.15ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (런타임 에러)
테스트 2 〉	실패 (런타임 에러)
테스트 3 〉	실패 (런타임 에러)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (런타임 에러)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
"""

# 이분 탐색
def solution(n):
    total = 0
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            total += 1
    
    return total
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 9.96MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 9.97MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 9.97MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
"""