class Solution:
    def partitionLabels(self, s: str):
        
        output = []
        seen = {}
        
        for i in range(len(s)):
            seen[s[i]] = i
            
        start  = 0
        end = 0
        
        for i in range(len(s)):
            end = max(end,seen[s[i]])
            
            if i == end:
                output.append(end - start + 1)
                start = end + 1
                
        return output


s = "ababcbacadefegdehijhklij"

c = Solution()
c.partitionLabels(s = s)
            
            