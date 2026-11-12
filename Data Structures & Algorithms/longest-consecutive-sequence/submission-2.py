class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        asap=set(nums)
        longest=0
        for num in asap:

            if num-1 not in asap:
                cur_num=num
                cur_len=1
            
                while cur_num+1 in asap:
                    cur_num+=1
                    cur_len+=1
            
                longest=max(longest,cur_len)

        return longest

