class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        def find(x):
            st = 0
            end = len(arr)-1
            while st<=end:
                mid = (st+end)//2
                if arr[mid]==x:
                    return True
                elif arr[mid]>x:
                    end = mid-1
                else:
                    st = mid+1
            return False
        for i in arr:
            if find(2*i):
                if 2*i != i or arr.count(i) > 1:
                    return True
        return False
        