class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first need to make s lower case
        # ex dood
        string = "".join(filter(str.isalnum,s)).lower()
        check = ""
        for i in range(len(string) - 1, -1, -1):
            check += string[i]
            print(check)
        return string == check
