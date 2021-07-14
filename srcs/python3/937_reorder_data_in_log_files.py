class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        llog=[]
        dlog=[]
        for log in logs:
            k = log.split()[0]
            v = log.split()[1:]

            if v[0].isdigit():
                # digit log
                dlog.append([k, v])
            else:
                # letter log
                llog.append([k, v])
            
        sort = sorted(llog, key=lambda x:(x[1],x[0]))
        for t in dlog:
            sort.append(t)
        
        answer=[]
        for log in sort:
            answer.append(log[0]+' '+' '.join(log[1]))
        return answer
