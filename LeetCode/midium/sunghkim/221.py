class Solution(object):
    
    def maximalSquare(self, matrix):
        M = len(matrix[0])
        N = len(matrix)
        matrix = [list(map(int,x)) for x in matrix]
        chleo = 0
        chleo2 = 0
        '''
        if N == 1 or M == 1:
            if [1] in matrix or 1 in matrix[0]:
                return (1)
            return (0)
        if N == 2 and M == 2:
            i = sum(matrix[0])
            i += sum(matrix[1])
            if i < 4:
                return (int(i >= 1))
            return (4)'''
        
        for i in range(1, N):
            for j in range(1, M):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                chleo = max(matrix[i][j], chleo)
        
        for i in matrix[0]:
            if i == 1:
                chleo = max(chleo, 1)
                break
        for i in matrix:
            if i[0] == 1:
                chleo = max(chleo, 1)
                break
                
        return (chleo * chleo)