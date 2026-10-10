class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch,0) + 1
        
        window = {}
        missing = len(t)
        left = 0
        best_start = 0
        best_len = float('inf')

        for right in range(len(s)):
            ch = s[right]

            if ch in need:
                window[ch] = window.get(ch,0) + 1

                if window[ch] <= need[ch]:
                    missing -= 1
            
            while missing == 0:

                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left
                
                left_ch = s[left]
                if left_ch in need:
                    window[left_ch] -= 1

                    if window[left_ch] < need[left_ch]:
                        missing += 1
                
                left += 1
        if best_len == float('inf'):
            return ""
        return s[best_start:best_start + best_len]

            

        