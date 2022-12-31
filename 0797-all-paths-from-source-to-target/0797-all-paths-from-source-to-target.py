class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def backtrack(i, curPath, allpaths):
            if i == len(graph)-1:
                return allpaths.append(list(curPath))
            
            for nn in graph[i]:
                curPath.append(nn)
                backtrack(nn, curPath, allpaths)
                curPath.pop() 
            
        allPaths = []
        backtrack(0, [0], allPaths)
    
        return allPaths


            

            

                
