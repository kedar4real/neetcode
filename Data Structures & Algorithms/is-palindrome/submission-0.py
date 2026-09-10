class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''#initialise new string
        #then we iterate through the string
        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        return newStr==newStr[::-1]

        