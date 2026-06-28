class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals, freeStart, freeEnd):

        occupiedIntervals.sort()
        

        merged = []
        for start, end in occupiedIntervals:
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        

        result = []
        for start, end in merged:

            if end < freeStart or start > freeEnd:
                result.append([start, end])

            elif freeStart <= start and freeEnd >= end:
                continue

            elif start < freeStart and end > freeEnd:
                result.append([start, freeStart - 1])
                result.append([freeEnd + 1, end])
  
            elif start < freeStart:
                result.append([start, freeStart - 1])
       
            elif end > freeEnd:
                result.append([freeEnd + 1, end])
        
        return result


      




        
        