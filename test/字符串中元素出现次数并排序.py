from collections import Counter


def conter_func(str1):
    # Counter 可以获取列表中元素出现的次数
    # most_common 可以获取出现最多的几个元素
    b = Counter(list(str1)).most_common(1)[0]
    str1 = str1.replace(b[0], '')
    if str1 and b[1] > 1:
        print('{0} {1}'.format(b[0], b[1]))
        return conter_func(str1)


str1 = 'agbmc34desf3gg4ghgmgw1ee5igkl2mmm'
conter_func(str1)
