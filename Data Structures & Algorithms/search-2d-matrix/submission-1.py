# You are given an m x n 2-D integer array matrix and an integer target.Each row in matrix is sorted in non-decreasing order.The first integer of every row is greater than the last integer of the previous row. Return true if target exists within matrix or false otherwise.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        row = -1

        while top <= bot:
            mid = top + (bot - top) // 2
            if target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                row = mid
                break

        if row == -1:
            return False

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


# Pattern: Two-Pass Binary Search (find candidate row via boundary checks, then search column)
# Time: O(log(m * n)) | Space: O(1)
