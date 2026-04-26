class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list) # (array, words(str[i]
        for string in strs:
            lst = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                lst[index] += 1
            hashmap[tuple(lst)].append(string)

        return list(hashmap.values())