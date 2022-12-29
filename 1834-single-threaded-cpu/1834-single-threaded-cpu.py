from heapq import * 

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        pendingTasks = [(i, task) for i, task in enumerate(tasks)]
        pendingTasks.sort(key=lambda x: x[1][0], reverse=True) 
        
        taskheap = [] 
        i = 0 
        res = [] 
        
        while True:
            while pendingTasks and pendingTasks[-1][1][0] <= i:
                readyTask = pendingTasks.pop()
                heappush(taskheap, (readyTask[1][1], readyTask[0]))
            
            if taskheap:
                processTask = heappop(taskheap)
                i += processTask[0]
                res.append(processTask[1])
            else:
                if not pendingTasks:
                    break
                i = pendingTasks[-1][1][0]

            if len(res) == len(tasks):
                break 
            
        
        return res 



                
            
            

