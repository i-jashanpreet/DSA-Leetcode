class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row = 0
        end_row = len(matrix) - 1
        
        while start_row <= end_row:
            mid_row = (start_row + end_row) // 2
        
            if matrix[mid_row][0] <= target <= matrix[mid_row][len(matrix[0]) - 1]:
                
                st = 0
                end = len(matrix[0]) - 1
                
                while st <= end:
                    mid = (st + end) // 2
                    
                    if matrix[mid_row][mid] == target:
                        return True
                    elif matrix[mid_row][mid] > target:
                        end = mid - 1
                    else:
                        st = mid + 1
                        
                return False  
            
            elif target > matrix[mid_row][-1]:
                start_row = mid_row + 1
            else:
                end_row = mid_row - 1
        
        return False
        
        