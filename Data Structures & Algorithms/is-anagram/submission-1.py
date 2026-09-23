class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Quick check - agar length alag hai, seedha False
        if len(s) != len(t):
            return False
        
        # Step 2: s ke letters ka count banao
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        # Step 3: t ke letters ka count ghatao
        for ch in t:
            count[ch] = count.get(ch, 0) - 1
        
        # Step 4: agar sab kuch sahi match hua, to saare counts 0 honge
        for value in count.values():
            if value != 0:
                return False
        
        return True