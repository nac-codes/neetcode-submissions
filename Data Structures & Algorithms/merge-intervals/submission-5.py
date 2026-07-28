class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # extend left, extend right, eaten, no-op

        M = 0
        for interval in intervals:
            M = max(M, interval[1])
        
        # could also set as a constraint constant of M, 1000

        number_line = [0] * (M * 2 + 1)

        for interval in intervals:
            start, end = interval[0], interval[1]
            if start == end:
                number_line[start*2] = 1
                continue
            
            start, end = interval[0]*2+1, interval[1]*2-1        
            while start <= end:
                number_line[start] = 1
                start += 2

        return_list = []    
        interval = []  
        for i in range(1,len(number_line), 2):            
            if len(interval) == 0:
                if number_line[i] == 1:
                    interval.append(int((i-1)/2))
                    interval.append(interval[0]+1)
            else:
                if number_line[i] == 1:
                    interval[1] = int((i+1)/2)
                else:
                    return_list.append(interval)
                    interval = []
        if interval:
            interval[1] = int(len(number_line)/2)
            return_list.append(interval)

        for i in range(0,len(number_line), 2):
            if number_line[i] == 1:
                if (i-1 < 0 and number_line[i+1] != 1) or (i+1 >= len(number_line) and number_line[i-1] != 1) or (number_line[i-1] != 1 and number_line[i+1] != 1):
                    return_list.append([int(i/2),int(i/2)])

                
        
        return return_list
            




