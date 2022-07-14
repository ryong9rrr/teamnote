function solution(s) {
  let stack = []
  for (const char of s) {
    if (stack && stack[stack.length - 1] === char) {
      stack.pop()
    } else {
      stack.push(char)
    }
  }
  return stack.length === 0 ? 1 : 0
}

// 정확성  테스트
// 테스트 1 〉	통과 (0.05ms, 30.4MB)
// 테스트 2 〉	통과 (18.13ms, 35.6MB)
// 테스트 3 〉	통과 (7.38ms, 36MB)
// 테스트 4 〉	통과 (9.68ms, 36MB)
// 테스트 5 〉	통과 (7.97ms, 36.4MB)
// 테스트 6 〉	통과 (8.38ms, 36.3MB)
// 테스트 7 〉	통과 (7.98ms, 36.3MB)
// 테스트 8 〉	통과 (7.79ms, 36.1MB)
// 테스트 9 〉	통과 (0.08ms, 30.4MB)
// 테스트 10 〉	통과 (0.08ms, 30MB)
// 테스트 11 〉	통과 (0.05ms, 30.2MB)
// 테스트 12 〉	통과 (0.08ms, 30MB)
// 테스트 13 〉	통과 (0.18ms, 29.9MB)
// 효율성  테스트
// 테스트 1 〉	통과 (50.87ms, 53.7MB)
// 테스트 2 〉	통과 (64.23ms, 37MB)
// 테스트 3 〉	통과 (37.44ms, 46.5MB)
// 테스트 4 〉	통과 (35.61ms, 46.4MB)
// 테스트 5 〉	통과 (33.12ms, 46.6MB)
// 테스트 6 〉	통과 (34.88ms, 46.4MB)
// 테스트 7 〉	통과 (36.06ms, 46.5MB)
// 테스트 8 〉	통과 (37.37ms, 53.1MB)
