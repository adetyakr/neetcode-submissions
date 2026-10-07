class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            

            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
        return max_length
        