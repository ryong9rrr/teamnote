from collections import defaultdict
def solution(n, lost, reserve):
    result = n - len(lost)
    
    students = defaultdict(int)
    
    for i in range(1, n + 1):
        students[i] = 1
    
    for i in lost:
        students[i] -= 1
    
    for i in reserve:
        students[i] += 1
        
    for i in range(1, n + 1):
        if students[i] == 0:
            if students[i - 1] >= 2:
                students[i] += 1
                students[i - 1] -= 1
            elif students[i + 1] >= 2:
                students[i] += 1
                students[i + 1] -= 1
    result = 0
    for i in range(1, n + 1):
        if students[i] >= 1:
            result += 1
            
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
"""