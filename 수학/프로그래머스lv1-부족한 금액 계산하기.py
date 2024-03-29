def solution(price, money, count):
    """
    # 등차수열문제
    # a = price, d = price
    # n번째 항 => a + (n-1)d => price + (n-1)price
    # n번째 항까지의 합(등차수열의 합)
    1. n(a + l) / 2 (l은 마지막항)
    2. n{2a + (n-1)d} / 2
    """
    # 등차수열의 마지막 항
    l = price * count

    # 등차수열의 합: n{2a + (n-1)d} / 2
    total = count * (price + l) // 2
    
    return total - money if money < total else 0
    
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.4MB)
테스트 15 〉	통과 (0.00ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.2MB)
테스트 20 〉	통과 (0.00ms, 10.3MB)
테스트 21 〉	통과 (0.00ms, 10.2MB)
테스트 22 〉	통과 (0.00ms, 10.2MB)
테스트 23 〉	통과 (0.00ms, 10.3MB)
"""