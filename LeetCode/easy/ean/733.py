class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        color = image[sr][sc]
        if color == newColor:
            return image
        image[sr][sc] = newColor
        stack = [[sr, sc, 0]]
        while stack:
            top = stack[-1]
            if top[2] > 3:
                stack.pop()
                continue
            nr, nc = top[0] + directions[top[2]][0], top[1] + directions[top[2]][1]
            if 0 <= nr and nr < m and 0 <= nc and nc < n and image[nr][nc] == color:
                image[nr][nc] = newColor
                stack.append([nr, nc, 0])
            else:
                top[2] += 1
        return image
