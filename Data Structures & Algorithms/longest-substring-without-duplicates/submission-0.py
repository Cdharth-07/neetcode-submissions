class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_lenght = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            current_window_size = right - left +1
            max_lenght = max(max_lenght, current_window_size)

        return max_lenght        