from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = Counter(tasks)

        all_tasks = len(tasks)


        # 算最高頻的任務有幾次
        max_task_type = max(list(a.values()))

        # 算有幾種任務達到最高頻次
        max_count_tasks = list(a.values()).count(max_task_type)

        # 算框架 最大任務數 -1 (最後一次不用冷卻) * n+1 (冷卻數+任務本身) + 1 (前面減掉的1)
        frame = (max_task_type - 1) * (n + 1) + max_count_tasks

        # 跟len(tasks)取max (對n=0的狀況)
        ans = max(frame, all_tasks)

        return ans

        





tasks  = ["A","A","A","B","B","B"]
n = 2


a = Solution()
b = a.leastInterval(tasks, n)
print(b)

