from collections import deque
import math
def solution(progresses, speeds):
    n = len(progresses)
    q = deque()
    for i in range(n):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    # 1번 기능이 처음 기준이 됨
    current = q.popleft()
    # 첫 날 릴리즈할 기능의 개수
    result = [1]
    while q:
        x = q.popleft()
        # 함께 릴리즈를 할 수 있다면 +1
        if x <= current:
            result[-1] += 1
        # 그렇지 않다면 새롭게 릴리즈
        else:
            current = x
            result.append(1)
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
"""

# 다시 풀었는데 옛날에 푼 방법이 더 참신한듯?
from collections import deque
import math
def solution(progresses, speeds):
    n = len(progresses)
    q = deque()
    for i in range(n):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))
    result = []
    current = q[0]
    count = 0
    while q:
        x = q.popleft()
        if x <= current:
            count += 1
        else:
            result.append(count)
            current = x
            count = 1
        if not q:
            result.append(count)
    return result


# 자바스크립트 - shift()를 사용했을 때
"""js
function solution(progresses, speeds) {
    const q = [];
    for (let i = 0; i < speeds.length; i++){
        q.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    let prev = q.shift()
    let result = [1]
    while (q.length > 0){
        const x = q.shift()
        if (prev >= x) {
            result[result.length - 1]++;
        } else {
            result.push(1)
            prev = x;
        }
    }
    return result
}

정확성  테스트
테스트 1 〉	통과 (0.06ms, 30MB)
테스트 2 〉	통과 (0.13ms, 30.3MB)
테스트 3 〉	통과 (0.09ms, 30.3MB)
테스트 4 〉	통과 (0.09ms, 30.4MB)
테스트 5 〉	통과 (0.09ms, 30.2MB)
테스트 6 〉	통과 (0.10ms, 30.4MB)
테스트 7 〉	통과 (0.16ms, 30.3MB)
테스트 8 〉	통과 (0.10ms, 30.2MB)
테스트 9 〉	통과 (0.09ms, 30.3MB)
테스트 10 〉	통과 (0.10ms, 30.2MB)
테스트 11 〉	통과 (0.08ms, 30.3MB)
"""

# 큐를 뒤집어서 스택처럼 사용했을 때
"""js
function solution(progresses, speeds) {
    const q = [];
    for (let i = 0; i < speeds.length; i++){
        q.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    q.reverse() // shift 연산을 사용하지 않기 위해
    let prev = q.pop()
    let result = [1]
    while (q.length > 0){
        const x = q.pop()
        if (prev >= x) {
            result[result.length - 1]++;
        } else {
            result.push(1)
            prev = x;
        }
    }
    return result
}

정확성  테스트
테스트 1 〉	통과 (0.07ms, 30.1MB)
테스트 2 〉	통과 (0.11ms, 30.3MB)
테스트 3 〉	통과 (0.11ms, 30.4MB)
테스트 4 〉	통과 (0.12ms, 30.4MB)
테스트 5 〉	통과 (0.09ms, 30.2MB)
테스트 6 〉	통과 (0.07ms, 30.2MB)
테스트 7 〉	통과 (0.10ms, 30MB)
테스트 8 〉	통과 (0.09ms, 30.3MB)
테스트 9 〉	통과 (0.08ms, 30.5MB)
테스트 10 〉	통과 (0.09ms, 30.3MB)
테스트 11 〉	통과 (0.06ms, 30.1MB)
"""