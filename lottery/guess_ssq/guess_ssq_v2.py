# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from collections import Counter
import sys
import os
import csv
import math

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
            tempCsvDatas = []
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
    # print(os.getcwd())
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

def counterBall(arr, d_arr):
    for i in range(0, len(d_arr)):
        d = d_arr[i]
        if d in arr:
            arr[d] = arr[d] + 1
        else:
            arr[d] = 1
    return arr

# 单式
def isWinSingle(a_arr, my_arr):
    a_blue = a_arr[-1]
    a_arr.pop()
    a_reds = sorted(a_arr)

    b_blue = my_arr[-1]
    my_arr.pop()
    b_reds = sorted(my_arr)

    # print(a_reds,a_blue)
    # print(b_reds,b_blue)
    if(len(a_reds) < 6 and len(b_reds) < 6):
        print("isWinSingle wrong data")
        return 0

    red_same = 0
    is_blue_same = False
    win_type = 0
    for i in range(0,6):
        if a_reds[i] == b_reds[i]:
            red_same = red_same + 1

    if(a_blue == b_blue):
        is_blue_same = True

    # print(red_same,is_blue_same)
    if is_blue_same:
        win_type = 6
        if red_same >= 3:
            win_type = 5
        if red_same >= 4:
            win_type = 4
        if red_same >= 5:
            win_type = 3
        if red_same >= 6:
            win_type = 1
    else:
        win_type = 0
        if red_same >= 4:
            win_type = 5
        if red_same >= 5:
            win_type = 4
        if red_same >= 6:
            win_type = 2

    return win_type

def testWin(a_arr, my_arr, winArr):
    getWinType = isWinSingle(a_arr, my_arr)
    if len(winArr) >= 7:
        loseSum = winArr[0]
        winOneSum = winArr[1]
        winTwoSum = winArr[2]
        winThreeSum = winArr[3]
        winFourSum = winArr[4]
        winFiveSum = winArr[5]
        winSixSum = winArr[6]
    else:
        loseSum = 0
        winOneSum = 0
        winTwoSum = 0
        winThreeSum = 0
        winFourSum = 0
        winFiveSum = 0
        winSixSum = 0
    if getWinType == 0:
        loseSum = loseSum + 1
        winArr[0] = loseSum
        # return "没中奖"
    elif getWinType == 1:
        winOneSum = winOneSum + 1
        winArr[1] = winOneSum
        # return "一等奖"
    elif getWinType == 2:
        winTwoSum = winTwoSum + 1
        winArr[2] = winTwoSum
        # return "二等奖"
    elif getWinType == 3:
        winThreeSum = winThreeSum + 1
        winArr[3] = winThreeSum
        # return "三等奖"
    elif getWinType == 4:
        winFourSum = winFourSum + 1
        winArr[4] = winFourSum
        # return "四等奖"
    elif getWinType == 5:
        winFiveSum = winFiveSum + 1
        winArr[5] = winFiveSum
        # return "五等奖"
    elif getWinType == 6:
        winSixSum = winSixSum + 1
        winArr[6] = winSixSum
        # return "六等奖"
    print("获得一等奖%s次,二等奖%s次,三等奖%s次,四等奖%s次,五等奖%s次,六等奖%s次,没获奖%s次"%(winOneSum,winTwoSum,winThreeSum,winFourSum,winFiveSum,winSixSum,loseSum))
    return winArr

# 获取历年的球总数
def getSumData(arr):
    arr_r = {}
    arr_b = {}
    for row_num in range(1, len(arr)):
        r1 = arr[row_num][2]
        r2 = arr[row_num][3]
        r3 = arr[row_num][4]
        r4 = arr[row_num][5]
        r5 = arr[row_num][6]
        r6 = arr[row_num][7]
        b1 = arr[row_num][8]
        # print("%s %s %s %s %s %s %s"%(r1,r2,r3,r4,r5,r6,b1))
        arr_r = counterBall(arr_r, [r1, r2, r3, r4, r5, r6])
        arr_b = counterBall(arr_b, [b1])
    new_r = sorted(arr_r.items(), key=lambda x:x[0], reverse = False)
    new_b = sorted(arr_b.items(), key=lambda x:x[0], reverse = False)
    print(new_r)
    print(new_b)

    # 保存文件
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    os.chdir(abspath)
    new_r_path = abspath + "/ssq_SUM_Redballs.csv"
    new_b_path = abspath + "/ssq_SUM_Blueballs.csv"

    cont_r_arr = []
    cont_b_arr = []
    for key,value in new_r:
        temp = []
        temp.append(key)
        temp.append(value)
        cont_r_arr.append(temp)
        # print(key,value)
    for key,value in new_b:
        temp = []
        temp.append(key)
        temp.append(value)
        cont_b_arr.append(temp)
        # print(key,value)

    Write2CSV(new_r_path, ["红球号码","总数"], cont_r_arr)
    Write2CSV(new_b_path, ["蓝球号码","总数"], cont_b_arr)

# 获取每一年的球总数  
def getEachSumData(arr):
    year_arr = {}
    year_total_arr = {}
    for row_num in range(1, len(arr)):
        y = arr[row_num][1]
        r1 = arr[row_num][2]
        r2 = arr[row_num][3]
        r3 = arr[row_num][4]
        r4 = arr[row_num][5]
        r5 = arr[row_num][6]
        r6 = arr[row_num][7]
        b1 = arr[row_num][8]

        df = math.floor(int(y) / 1000)

        # 计算每一年有几个数据
        if df in year_total_arr:
            year_total_arr[df] = year_total_arr[df] + 1
        else:
            year_total_arr[df] = 1

        if df in year_arr:
            d = year_arr[df]
            arr_r = d["red_balls"]
            arr_b = d["blue_balls"]
            arr_r = counterBall(arr_r, [r1, r2, r3, r4, r5, r6])
            arr_b = counterBall(arr_b, [b1])
            d["red_balls"] = arr_r
            d["blue_balls"] = arr_b
        else:
            arr_r = {}
            arr_b = {}
            year_arr[df] = {}
            d = year_arr[df]
            arr_r = counterBall(arr_r, [r1, r2, r3, r4, r5, r6])
            arr_b = counterBall(arr_b, [b1])
            d["red_balls"] = arr_r
            d["blue_balls"] = arr_b

    # print(year_total_arr)
    # print(year_arr)

    # 保存文件
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    os.chdir(abspath)
    for key in year_arr:
        # print(key,year_arr[key])
        r_path = abspath + "/ssq_year(%s)_SUM_Redballs.csv"%(key)
        b_path = abspath + "/ssq_year(%s)_SUM_Blueballs.csv"%(key)

        d1 = year_arr[key]["red_balls"]
        d2 = year_arr[key]["blue_balls"]
        new_r = sorted(d1.items(), key=lambda x:x[0], reverse = False)
        new_b = sorted(d2.items(), key=lambda x:x[0], reverse = False)
        # print(new_r)
        # print(new_b)

        cont_r_arr = []
        cont_b_arr = []
        for key,value in new_r:
            temp = []
            temp.append(key)
            temp.append(value)
            cont_r_arr.append(temp)
            # print(key,value)
        for key,value in new_b:
            temp = []
            temp.append(key)
            temp.append(value)
            cont_b_arr.append(temp)
            # print(key,value)

        Write2CSV(r_path, ["红球号码","总数"], cont_r_arr)
        Write2CSV(b_path, ["蓝球号码","总数"], cont_b_arr)

# 获取历年的球准确率
def getDataRightRate(arr,mode=1):
    if mode == 3:
        winA = getDataRightRate(arr,1)
        winB = getDataRightRate(arr,1)
        winA[0] = 0
        for i in range(0, len(winA)):
            winA[i] = winA[i] + winB[i]
        print(winA)
    else:
        red_num = []
        blue_num = []
        winArr = [0,0,0,0,0,0,0]
        for i in range(1,len(arr)-1):
            red_num.append(arr[i][2])
            red_num.append(arr[i][3])
            red_num.append(arr[i][4])
            red_num.append(arr[i][5])
            red_num.append(arr[i][6])
            red_num.append(arr[i][7])
            blue_num.append(arr[i][8])
            red_count = Counter(red_num)
            blue_count = Counter(blue_num)

            # 正选
            if mode == 1:
                red_count_sorted = sorted(red_count.items(), key=lambda pair: pair[1], reverse=False)
                blue_count_sorted = sorted(blue_count.items(), key=lambda pair: pair[1], reverse=False)
            # 反选
            elif mode == 2:
                red_count_sorted = sorted(red_count.items(), key=lambda pair: pair[1], reverse=True)
                blue_count_sorted = sorted(blue_count.items(), key=lambda pair: pair[1], reverse=True)

            ssq_red = red_count_sorted[0:6]
            ssq_blue = blue_count_sorted[0:3]
            ssq_red = list(map(lambda item:item[0], ssq_red))
            ssq_blue = list(map(lambda item:item[0], ssq_blue))
            ssq_red.sort()
            ssq_blue.sort()
            # print(i,ssq_red,ssq_blue)

            expected_arr = []
            next_arr = []
            if arr[i+1]:
                next_arr.append(arr[i+1][2])
                next_arr.append(arr[i+1][3])
                next_arr.append(arr[i+1][4])
                next_arr.append(arr[i+1][5])
                next_arr.append(arr[i+1][6])
                next_arr.append(arr[i+1][7])
                next_arr.append(arr[i+1][8])
                if len(ssq_blue)>0:
                    expected_arr = ssq_red
                    expected_arr.append(ssq_blue[0])
                    winArr = testWin(next_arr, expected_arr, winArr)
                elif len(ssq_blue)>1:
                    expected_arr = ssq_red
                    expected_arr.append(ssq_blue[1])
                    winArr = testWin(next_arr, expected_arr, winArr)
                elif len(ssq_blue)>2:
                    expected_arr = ssq_red
                    expected_arr.append(ssq_blue[2])
                    winArr = testWin(next_arr, expected_arr, winArr)
            
        t = 0
        for j in range(1,len(winArr)-1):
            t = winArr[j] + t
        rate = t / winArr[0]
        print(rate)
        return winArr

def analysisData(arrays):
    # getSumData(arrays)
    # getEachSumData(arrays)
    getDataRightRate(arrays,3)

if __name__ == "__main__":
    # 获取数据
    # getWebContent()

    # 读取数据
    array = ReadCSV()

    # 分析数据
    analysisData(array)