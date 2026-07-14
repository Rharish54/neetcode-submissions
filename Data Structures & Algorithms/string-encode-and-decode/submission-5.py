class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + "`" + s
        
        return res
        #output should be *neet*code*love*you

    def decode(self, s: str) -> List[str]:
        
        if s == "`":
            return [""]
        s = s[1:]
        output = []
        temp = ""
        for i, ch in enumerate(s):
            print(temp)
            if i == len(s) - 1:
                temp = temp + ch
                output.append(temp)
            elif ch == '`':
                output.append(temp)
                temp = ""
            else:
                temp = temp + ch
        
        return output
