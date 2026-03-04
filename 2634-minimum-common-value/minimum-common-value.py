class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def find(arr,x):
            st = 0
            end = len(arr)-1
            ans = False
            while st<=end:
                mid = (st+end)//2
                if arr[mid]==x:
                    ans = True
                    return ans
                elif arr[mid]>x:
                    end = mid-1
                else:
                    st = mid+1
            return ans
        small = -1
        for i in nums1:
            if find(nums2,i):
                if small == -1 or i<small:
                    small = i
        return small

