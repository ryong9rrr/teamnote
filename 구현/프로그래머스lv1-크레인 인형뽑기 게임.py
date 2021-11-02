import numpy as np
def solution(board, moves):
    LEN = len(board)
    board_cols = np.array(board)
    new_board = []
    for i in range(LEN) :
        new_board.append( list(reversed([x for x in board_cols[:,i] if x!=0])) )
        
    print( new_board )
    
    count = 0
    basket = []
    for move in moves :
        if len(new_board[move-1]) != 0 :
            basket.append( new_board[move-1].pop() )
            if len(basket) >= 2 :
                if basket[-1] == basket[-2] :
                    basket.pop()
                    basket.pop()
                    count += 2
    return count

"""
정확성  테스트
테스트 1 〉	통과 (0.13ms, 27.7MB)
테스트 2 〉	통과 (0.07ms, 27.7MB)
테스트 3 〉	통과 (0.07ms, 27.7MB)
테스트 4 〉	통과 (0.94ms, 27.9MB)
테스트 5 〉	통과 (0.12ms, 27.8MB)
테스트 6 〉	통과 (0.10ms, 27.9MB)
테스트 7 〉	통과 (0.15ms, 27.8MB)
테스트 8 〉	통과 (0.46ms, 27.7MB)
테스트 9 〉	통과 (0.38ms, 27.9MB)
테스트 10 〉	통과 (0.39ms, 27.9MB)
테스트 11 〉	통과 (0.79ms, 28MB)
"""

from collections import deque
def solution(board, moves):
    result = 0
    #인형이 담길 배열
    stack = deque()
    b = len(board)
    for j in moves:
        for i in range(b):
            if board[i][j-1] != 0:
                x = board[i][j-1]
                board[i][j-1] = 0
                if stack and x == stack[-1]:
                    result += 2
                    stack.pop()
                    break
                stack.append(x)
                break
    return result

"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (1.12ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.07ms, 10.2MB)
테스트 8 〉	통과 (0.28ms, 10.3MB)
테스트 9 〉	통과 (0.24ms, 10.2MB)
테스트 10 〉	통과 (0.29ms, 10.2MB)
테스트 11 〉	통과 (0.66ms, 10.4MB)
"""