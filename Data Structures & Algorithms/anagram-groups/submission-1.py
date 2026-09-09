class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups=defaultdict(list) 
        #word iterates through string
        for word in strs:
            key=''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())