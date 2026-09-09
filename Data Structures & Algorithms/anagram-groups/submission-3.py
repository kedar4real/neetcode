class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res=defaultdict(list)

        for word in strs:
            key=frozenset(Counter(word).items())
            res[key].append(word)
        return list(res.values())