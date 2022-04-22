s = "Race Car"


class Solution:
    
    def validate_palindrome(self,s):

        s = str(s).lower()
        start = 0
        end = len(s) - 1

        while start < end:
            
            if not s[start].isalnum() and start < end:
                start += 1
            if not s[end].isalnum() and start < end:
                end -= 1
            

            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
        
        return True


ss = Solution()

ss.validate_palindrome(s= s)
