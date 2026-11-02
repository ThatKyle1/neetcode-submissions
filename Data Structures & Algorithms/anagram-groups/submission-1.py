class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list) # (array, words(str[i]))
        for string in strs:
            count = [0] * 26
            for char in string:
                # use asci values to map indexs for count array ord - ord(a) will do this correctly
                count[ord(char) - ord('a')] += 1
            hashmap[tuple(count)].append(string) # have to convert to tuple for hashmap key
        return list(hashmap.values())


        
