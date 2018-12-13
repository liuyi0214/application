# Python 实现冒泡排序
def bubbleSort1(alist):
    for j in range(0,len(alist)):
        for i in range(1,len(alist)-j):
            if alist[i-1] > alist[i]:
                alist[i-1],alist[i] = alist[i],alist[i-1]
    return alist

alist = [54,26,93,17,77,31,44,55,20,13,6,17,77]
print(bubbleSort1(alist))

# Python 实现冒泡排序
def bubbleSort2(alist):
    for i in range(1,len(alist)):
        if alist[i-1] < alist[i]:
            alist[i-1],alist[i] = alist[i],alist[i-1]
    if alist:
        print(alist.pop(-1),end='  ')
        return bubbleSort2(alist)

alist = [54,26,93,17,77,31,44,55,20,13,6,17,77]
bubbleSort2(alist)