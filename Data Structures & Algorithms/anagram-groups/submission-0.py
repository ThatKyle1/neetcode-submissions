class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i, word in enumerate(strs):
            sorted_word = "".join(sorted(word)) # this sorts each word
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word) # add the original word to list
            else:
                hashmap[sorted_word] = [word]
        
        return list(hashmap.values())
