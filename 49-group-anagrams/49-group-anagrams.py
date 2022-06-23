class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWord = defaultdict(list)
        for word in strs:
            sortedWord[str(sorted(word))].append(word)
            
        return list(sortedWord.values())