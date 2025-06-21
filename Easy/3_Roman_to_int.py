"""
    Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and symbol_map[s[i]] < symbol_map[s[i + 1]]:
                total += symbol_map[s[i + 1]] - symbol_map[s[i]]
                i += 2
            else:
                total += symbol_map[s[i]]
                i += 1

        return total


sol = Solution()
print(sol.romanToInt("MCMXCIV"))