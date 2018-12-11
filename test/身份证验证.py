Factor = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
Last = ("1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2")

def id_check(id=input('输入id: ')):
    if Last[int(sum(int(id[i]) * Factor[i] for i in range(0, 17)) % 11)] == id[-1]:
        if int(id[-2])%2==0:
            print('性别: 女')
        else:print('性别 :男')
    else:
        print('错,重输')
        return id_check(id=input('输入id: '))

id_check()
