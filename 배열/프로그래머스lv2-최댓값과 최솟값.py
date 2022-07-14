# 리스트 컴프리헨션
def solution(s):
    numbers = [int(number) for number in s.split(" ")]
    return f"{min(numbers)} {max(numbers)}"

# map()
def solution(s):
    numbers = list(map(int, s.split(" ")))
    return f"{min(numbers)} {max(numbers)}"

"""
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.5MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.4MB)
"""