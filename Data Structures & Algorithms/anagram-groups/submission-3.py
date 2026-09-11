class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # key anagram, anagram will be a lst of how many char
        # value those same str anagram

        #first loop thru
        # get each str anagram combo
        # then see if it is in the hashmap if it is add to that list

        hashmap = defaultdict(list) # automaticall sets up the hashmap as a list
        for string in strs:
            anagram = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                anagram[index] += 1
            hashmap[tuple(anagram)].append(string)
        
        return list(hashmap.values())