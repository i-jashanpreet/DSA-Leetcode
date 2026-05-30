class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(left,right):
            i = 0
            j = 0
            n = len(left)
            m = len(right)
            arr = []
            while i<n and j<m:
                if left[i]<=right[j]:
                    arr.append(left[i])
                    i+=1
                else:
                    arr.append(right[j])
                    j+=1
            while i<n:
                arr.append(left[i])
                i+=1
            while j<m:
                arr.append(right[j])
                j+=1
            return arr
        ans = merge(nums1,nums2)
        n = len(ans)
        if n%2==1:
            return ans[n//2]
        else:
            return (ans[n//2]+ans[n//2-1])/2
        
        