def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
        # tmp = []
        # for i in range(len(N)):
        #     a = N[i-1] + N[i]
        #     print('a',N)
        #     tmp.append(a)
        # N = tmp

res = triangles()
res.__iter__()
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
