from typing import List

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # 如果顏色相同就出去
        origin_color = image[sr][sc]
        if origin_color == color:
            return image
        
        def fill(r, c):
            # 小於0或超出原圖片範圍，r對image  c對image[0]
            if r<0 or r>=len(image) or c<0 or c>=len(image[0]):
                return

            # 原圖相鄰數字如果不同，則滾蛋
            if image[r][c] != origin_color:
                return
            
            image[r][c] = color

            fill(r+1, c)
            fill(r-1, c)
            fill(r, c+1)
            fill(r, c-1)


        fill(sr, sc)
        return image


image = [[0,0,0],[0,0,0]]
sr = 1
sc = 0
color = 2

a = Solution()
b = a.floodFill(image, sr, sc, color)
print(b)
