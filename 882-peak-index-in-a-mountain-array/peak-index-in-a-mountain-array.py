class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        start=0
        end=n-1
        ans=-1
        while start<=end:
            mid=(start+end)//2
            if mid<n-1 and arr[mid]<arr[mid+1]:
                start=mid+1
            else:
                end=mid-1
                ans=mid
        return ans     