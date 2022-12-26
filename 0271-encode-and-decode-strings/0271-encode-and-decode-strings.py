class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            delim = str(len(s)) 
            res = res + "0" * (3 - len(delim)) + delim + s
        return res 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        
        i = 0 
        while i < len(s):
            count = int(s[i: i+3])
            res.append(s[i+3: i+3+count])
            i = i + 3 + count

        return res 
