# 로그파일 재정렬
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        m_logs = []
        d_logs = []
        for log in logs:
            log_list = log.split()
            if log_list[1].isdigit():
                d_logs.append(log)
            else:
                m_logs.append(log_list)
        m_logs.sort(key = lambda x : (x[1:], x[0]))
        
        for logs in m_logs:
            result = ' '.join(log for log in logs)
            answer.append(result)
        for log in d_logs:
            answer.append(log)
        return answer

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        m_logs = []
        d_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                d_logs.append(log)
            else:
                m_logs.append(log)
        m_logs.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        
        return m_logs + d_logs