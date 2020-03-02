# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from collections import Counter
import sys
import os
import csv

# 写入数据到CSV
def Write2CSV(file_path, head_row, content_rows):
    f = open(file_path,'w',encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    # 构建列表头
    csv_writer.writerow(head_row)
    # 写入csv文件内容
    for i in range(len(content_rows)):
        csv_writer.writerow(content_rows[i])
    f.close()

# 读取csv
def ReadCSV():
    # 切换到当前执行文件的工作目录下
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    os.chdir(abspath)
    print(os.getcwd())
    file_path = abspath + "/ssq_sorted.csv"

    csvDatas = []
    tempCsvDatas = []
    with open(file_path,newline='',encoding='UTF-8') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            for i in row:
                tempCsvDatas.append(i)
            # print(','.join(row))
            csvDatas.append(tempCsvDatas)
    return csvDatas

def getWebContent():
    # 获取内容
    web_page = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
    res = requests.get(web_page, timeout = 30)
    res.encoding = 'utf-8'
    htm = res.text
    # 解析内容
    soup = BeautifulSoup(htm, 'html.parser')
    # url前缀
    prefix_url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list'
    #获取总页数
    total = int(soup.find('p', attrs={"class": "pg"}).find_all('strong')[0].text)

    # 切换到当前执行文件的工作目录下
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    os.chdir(abspath)
    print(os.getcwd())
    new_file_path = abspath + "/ssq_new.csv"
    sort_file_path = abspath + "/ssq_sorted.csv"

    #将获取的信息，写进文件
    red_num = [] #历史上开出的红球
    blue_num = [] #历史上开出的蓝球
    csv_data_array = []
    temp_data_array = []

    # 分页获取每一页的开奖信息
    for page_num in range(1, total+1):
        t_url = prefix_url + '_' + str(page_num) + '.html'
        print(t_url)
        res2 = requests.get(t_url, timeout = 30)
        res2.encoding = 'utf-8'
        page_context = res2.text
        page_soup = BeautifulSoup(page_context, 'html.parser')
        if page_soup.table is None:
            continue
        elif page_soup.table:
            table_rows = page_soup.table.find_all('tr')
            for row_num in range(2, len(table_rows)-1):
                row_tds = table_rows[row_num].find_all('td')
                ems = row_tds[2].find_all('em')
                result = row_tds[0].string +','+ row_tds[1].string +', '+ems[0].string+' '+ems[1].string+' '+ems[2].string+' '+ems[3].string+' '+ems[4].string+' '+ems[5].string+' '+ems[6].string
                print(result)
                red_num.append(ems[0].string) # 红球1
                red_num.append(ems[1].string) # 红球2
                red_num.append(ems[2].string) # 红球3
                red_num.append(ems[3].string) # 红球4
                red_num.append(ems[4].string) # 红球5
                red_num.append(ems[5].string) # 红球6
                blue_num.append(ems[6].string) # 蓝球

                temp_data_array.append(row_tds[0].string) # 开奖时间
                temp_data_array.append(row_tds[1].string) # 开奖期号
                temp_data_array.append(ems[0].string) # 红球1
                temp_data_array.append(ems[1].string) # 红球2
                temp_data_array.append(ems[2].string) # 红球3
                temp_data_array.append(ems[3].string) # 红球4
                temp_data_array.append(ems[4].string) # 红球5
                temp_data_array.append(ems[5].string) # 红球6
                temp_data_array.append(ems[6].string) # 蓝球
                csv_data_array.append(temp_data_array)
                temp_data_array = []
            else:
                continue

    # 重新整理 逆序存储
    sorted_data_array = csv_data_array.copy()
    sorted_data_array.reverse()

    # print(csv_data_array)
    head_row = ["开奖时间","开奖期号","红球1","红球2","红球3","红球4","红球5","红球6","蓝球"]
    Write2CSV(new_file_path, head_row, csv_data_array)
    Write2CSV(sort_file_path, head_row, sorted_data_array)

    red_count = Counter(red_num)
    blue_count = Counter(blue_num)
    # 按照出现频率顺序
    red_count_sorted = sorted(red_count.items(), key=lambda pair: pair[1], reverse=False)
    blue_count_sorted = sorted(blue_count.items(), key=lambda pair: pair[1], reverse=False)
    print(red_count_sorted)
    print(blue_count_sorted)

    ssq_red = red_count_sorted[0:6]
    ssq_blue = blue_count_sorted[0:3]
    print(list(map(lambda item:item[0], ssq_red)))
    print(list(map(lambda item:item[0], ssq_blue)))
    ssq_red = list(map(lambda item:item[0], ssq_red))
    ssq_blue = list(map(lambda item:item[0], ssq_blue))
    ssq_red.sort()
    ssq_blue.sort()
    print('顺选-1：'+str(ssq_red)+'|'+ssq_blue[0])
    print('顺选-2：'+str(ssq_red)+'|'+ssq_blue[1])
    print('顺选-3：'+str(ssq_red)+'|'+ssq_blue[2])
    print('------------------------------------------------------------------------------')
    # 按照出现频率倒序
    red_count_sorted = sorted(red_count.items(), key=lambda pair: pair[1], reverse=True)
    blue_count_sorted = sorted(blue_count.items(), key=lambda pair: pair[1], reverse=True)
    print(red_count_sorted)
    print(blue_count_sorted)

    ssq_red = red_count_sorted[0:6]
    ssq_blue = blue_count_sorted[0:3]
    print(list(map(lambda item:item[0], ssq_red)))
    print(list(map(lambda item:item[0], ssq_blue)))
    ssq_red = list(map(lambda item:item[0], ssq_red))
    ssq_blue = list(map(lambda item:item[0], ssq_blue))
    ssq_red.sort()
    ssq_blue.sort()
    print('反选-1：'+str(ssq_red)+'|'+ssq_blue[0])
    print('反选-2：'+str(ssq_red)+'|'+ssq_blue[1])
    print('反选-3：'+str(ssq_red)+'|'+ssq_blue[2])

def analysisData(arrays):

    for row_num in range(0, len(arrays)-1):
        # print(arrays[row_num])
        # for i in arrays

if __name__ == "__main__":
    # 获取数据
    # getWebContent()

    # 读取数据
    array = ReadCSV()
    # print(array)

    analysisData(array)