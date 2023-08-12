class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ''
        for string in strs:
            encoded= encoded+ str(len(string)) + '#'+ string
        #encoded = chr(258).join(strs)
        return encoded
            
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        last_start = 0
        decoded=[]
        while i < len(s):
            if s[i] == '#':
                length = int(s[last_start:i])
                decoded.append(s[i+1:i+length+1])
                last_start = i+length+1
                i +=length+1
            else:
                i +=1
        #decoded = s.split(sep= chr(258))
        return decoded