class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f = []
        j = 0
        k = 0
        while j < m and k < n:
            if nums1[j] < nums2[k]:
                f.append(nums1[j])
                j += 1
            elif nums2[k] < nums1[j]:
                f.append(nums2[k])
                k += 1
            else:
                f.append(nums1[j])
                j += 1
                f.append(nums2[k])
                k += 1
        while j < m:
            f.append(nums1[j])
            j += 1

        while k < n:
            f.append(nums2[k])
            k += 1
        for i in range(m + n):
            nums1[i] = f[i]
        
        