from typing import Optional, List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mid = m-1
        nid = n-1
        
        i = m+n-1
        
        while nid >=0:
            if mid>=0 and nums1[mid] > nums2[nid]:
                nums1[i] = nums1[mid]
                mid -=1
            
            else:
                nums1[i] = nums2[nid]
                nid -=1
            
            i -=1
