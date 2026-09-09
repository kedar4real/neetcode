class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups=defaultdict(list)

        for word in strs:
            key=''.join(sorted(word))
            groups[key].append(word)#adds the word to their respective key (which is sorted)ex tops and pots
        return list(groups.values())    