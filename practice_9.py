#请使用迭代查找一个list中的最小值和最大值，并返回一个tuple
def findMinAndMax(s):
    min=0
    max=0
    for i in s:
        if i>max:
            max=i
    for i in s:
        if i<min:
            min=i
    return max,min
print(findMinAndMax([2,3,-1,2,9,19,2]))
