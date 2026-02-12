class Solution:
    def search(self, arr: List[int], key: int) -> int:
        start = 0
        end = len(arr)-1
        while start<=end:
            mid = (start+end)//2
            if arr[mid]==key:
                return mid
            if arr[start]<=arr[mid]:
                if key>=arr[start] and key<=arr[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if key>=arr[mid] and key<=arr[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1
        