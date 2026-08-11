class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      

        hashtable = defaultdict(int)
        
        for i in nums:
            hashtable[i]+=1

        key = max(hashtable, key=hashtable.get)
        
        return key

        
        