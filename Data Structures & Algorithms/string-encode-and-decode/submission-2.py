import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        has_hash = 0
        encoded_text = ""
        for i, text in enumerate(strs):
            text_length = len(text)
            if "#" in "".join(strs):
                encoded_text += f"##{text_length}##" + text
                has_hash = 1
            else:
                encoded_text += f"#{text_length}#" + text
        if has_hash == 0:
            encoded_text += "#False"
            return encoded_text
        encoded_text += "#True"
        return encoded_text


    def decode(self, s: str) -> List[str]:
        result = []
        if s[-5:] == "#True":
            pattern = r"##\d+##"
            matches = re.finditer(pattern, s)
            for match in matches:
                word_length = int(match.group()[2:-2])
                word_start = match.end()
                word = s[word_start:word_start+word_length]
                result.append(word)

        else:
            pattern = r"#\d+#"
            matches = re.finditer(pattern, s)
            for match in matches:
                word_length = int(match.group()[1:-1])
                word_start = match.end()
                word = s[word_start:word_start+word_length]
                result.append(word)

        return result
