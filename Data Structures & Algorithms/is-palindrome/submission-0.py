class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''.join(i for i in s if i.isalnum())
        pes=res.lower()
        if pes==pes[::-1]:
            return True
        return False
        