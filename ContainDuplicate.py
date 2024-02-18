class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        conjunto = set()
        for n in nums:
            if n in conjunto:
                return True
            conjunto.add(n)
        return False 