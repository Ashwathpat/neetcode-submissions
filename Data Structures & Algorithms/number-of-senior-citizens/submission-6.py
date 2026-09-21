class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for cit in details:
            for i in range(len(cit)-2):
                if cit[i]=='M' or cit[i]=='F' or cit[i]=='O':
                    agestr=cit[i+1]+cit[i+2]
                    age=int(agestr)
                    if age>60:
                        count+=1
                    break
        return count