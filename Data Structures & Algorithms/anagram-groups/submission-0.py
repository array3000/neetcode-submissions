class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # same strat as anagrams, same letters so hash letters, but also hash the "group"
        # they're in, ex a,c,t (all of in group 0)
        # but this would require too much memory and assumptions

        groups = defaultdict(list) # letter array : group list (this is done to avoid an edgecase
        # which one?)

        for word in strs:
            # letters[26] # is this how you make a statically sized array?
            letters = [0] * 26 # no, this is how it is in python?
            for char in word:
                # assuming ascii, ord just turns it into ascii values
                # I thought += 1 was not allowed in python?
                letters[ord(char) - ord("a")] += 1
                #groups[letters[letterIndex]] = 1 + groups.get(letters[letterIndex], 0)
            # casted to tuples b/c tuples accepted as keys in dictionary
            groups[tuple(letters)].append(word)
        return list(groups.values())
                


         

        