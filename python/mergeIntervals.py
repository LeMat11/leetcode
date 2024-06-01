# Method 1
# def mergeIntervals(intervals):
#     if len(intervals) < 2:
#         return intervals 
#     intervals = sorted(intervals,key = lambda x:x[0])
#     for i in range(1,len(intervals)):
#         if intervals[i][0] <= intervals[i-1][1]:
#             intervals[i][0] = intervals[i-1][0]
#         if intervals[i][1] <= intervals[i-1][1]:
#             intervals[i][1] = intervals[i-1][1]
    
#     temp = intervals[i][0]
#     i -= 1

#     while i>=0:
#         if intervals[i][0] == temp:
#             intervals.remove(intervals[i])
#             i -= 1
#         else:
#             temp = intervals[i][0]
#             i -= 1
    
#     return intervals

# Method 2

def mergeIntervals(intervals):
    intervals = sorted(intervals,key = lambda x:x[0])
    res = []

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1],interval[1])

    return res

def main():
    res = mergeIntervals([[1,4],[0,4]])
    print(res)

main()

