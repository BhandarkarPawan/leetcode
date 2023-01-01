class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        
        if not intervals: 
            return True

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prevEnd: 
                return False 
            prevEnd = end
                        
        return True 