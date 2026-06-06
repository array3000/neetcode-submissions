class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Hashmaps of each
        Map_s, Map_t = {}, {}
        # build hashmap for S and T
        for i in range(len(s)):
            # prevents key error
            Map_s[s[i]] = 1 + Map_s.get(s[i], 0)
            Map_t[t[i]] = 1 + Map_t.get(t[i], 0)

        # compare both maps
        for char in Map_s:
            if Map_s[char] != Map_t.get(char, 0):
                return False
        #if hashmaps are identical, then anagram
        return True


            
        