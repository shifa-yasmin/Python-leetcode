class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums1[i] not in res:
                        res.append(nums1[i])
        return res