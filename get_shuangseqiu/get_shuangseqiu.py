#!/usr/bin/python
# -*- coding:UTF-8 -*-

import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

url_1 = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
url_2 = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_{0}.html'  # 调用新url链接获取球
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


def get_page_number_from_url() -> int:
    page = requests.get(url_1, headers=headers)
    soup = BeautifulSoup(page.text)
    strong = soup.find('td', colspan='7')
    if strong:
        result = strong.get_text()
        # 共118 页 /2348 条记录 首页 上一页 下一页 末页 当前第 1 页
        list_num = int(re.findall("[0-9]{1,3}", result)[0])
        print('共{0}页'.format(list_num))  # 获取共有多少页 180
        return list_num
    else:
        return 0


def get_data_from_rul(num):
    all_data_list = []  # type : list
    all_date_list = []  # type : list
    for num in range(1, num):
        page = BeautifulSoup(requests.get(url=url_2.format(num), headers=headers).text)
        em_list = page.find_all('em')  # 匹配em 含有球数字的内容 <em class="rr">05</em>
        div_list = page.find_all('td', {'align': 'center'})  # 匹配 <td align=center>这样的内容 匹配含有日期的数据
        # print('em_list', em_list)
        # print('div list', div_list)

        # 把匹配到的日期存到列表里
        for div in div_list:
            text = div.get_text().strip('')
            list_num = re.findall('\d{4}-\d{2}-\d{2}', text)
            if list_num:
                date = list_num[0]
                all_date_list.append(date)

        # 把匹配到的球存到列表里
        tmp_list = []  # type: list
        for div in em_list:
            text = div.get_text()
            if len(tmp_list) == 6:
                tmp_list.append(int(text))
                all_data_list.append(tmp_list)
                tmp_list = []
            else:
                tmp_list.append(int(text))
        del tmp_list

    #print(all_data_list)
    #print(all_date_list)
    # 把数据存入csv 时间做索引列
    df = pd.DataFrame(data=all_data_list, columns=[1, 2, 3, 4, 5, 6, 7], index=all_date_list)
    df.to_csv('shuangseqiu.csv', sep=',', index_label='DATE')


num = get_page_number_from_url()
get_data_from_rul(num)

#数据展示
df = pd.read_csv('shuangseqiu.csv')
print(df.head())