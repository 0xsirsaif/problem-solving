class Solution:
    def entityParser(self, text: str) -> str:
        special_chars = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
        }
        return "ss"


S = Solution()
print(S.entityParser(""))
