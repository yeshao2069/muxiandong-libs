# -*- coding: utf-8 -*-
import sys
import os
import csv
import xlrd,xlwt
import datetime


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

# 写入数据到Excel
def Write2Excel(file_path, sheet_name, contents):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(sheet_name)

    # 设置字体字样
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'Times New Roman' 
    font.bold = True # 黑体
    font.underline = True # 下划线
    font.italic = True # 斜体字
    style.font = font # 设定样式

    # 设置单元格宽度 256*N col(0)是第一列
    # ws.col(0).width = 256*20
    # 设置单元格高度 row(0)是第一行
    # tall_style = xlwt.easyxf('font:height 720;') # 36pt,类型小初的字号 
    # ws.row(0).set_style(tall_style)

    # 输入一个日期到单元格
    # style.num_format_str = 'M/D/YY' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
    # ws.write(0, 4, datetime.datetime.now(), style)

    # 添加一个公式
    # ws.write(0, 4, 5) # Outputs 5
    # ws.write(0, 5, 2) # Outputs 2
    # ws.write(1, 4, xlwt.Formula('E1*F1')) # Should output "10" (A1[5] * A2[2])
    # ws.write(1, 5, xlwt.Formula('SUM(E1,F1)')) # Should output "7" (A1[5] + A2[2])

    # 添加一个超链接
    # ws.write(0, 4, xlwt.Formula('HYPERLINK("https://www.baidu.com";"BaiDu")')) # Outputs the text "BaiDu" linking to https://www.baidu.com

    # 设置对齐方式
    # alignment = xlwt.Alignment() # Create Alignment
    # alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    # alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
    # style = xlwt.XFStyle() # Create Style
    # style.alignment = alignment # Add Alignment to Style
    # ws.write(0, 4, 'aa', style)

    # 添加单元格边框
    # borders = xlwt.Borders() # Create Borders
    # borders.left = xlwt.Borders.DASHED # DASHED虚线 NO_LINE没有 THIN实线
        
    # # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
    # borders.right = xlwt.Borders.DASHED
    # borders.top = xlwt.Borders.DASHED
    # borders.bottom = xlwt.Borders.DASHED
    # borders.left_colour = 0x40
    # borders.right_colour = 0x40
    # borders.top_colour = 0x40
    # borders.bottom_colour = 0x40
    # style = xlwt.XFStyle() # Create Style
    # style.borders = borders # Add Borders to Style
    # ws.write(0, 4, 'bb', style)

    # 添加背景色
    pattern = xlwt.Pattern() # Create the Pattern
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
    pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
    style = xlwt.XFStyle() # Create the Pattern
    style.pattern = pattern # Add Pattern to Style
    ws.write(0, 4, 'cc', style)

    for i in range(len(contents)):
        for j in range(len(contents[i])):
            ws.write(i, j, label=contents[i][j]) # 不带样式的写入
            # ws.write(i, j, contents[i][j], style) # 带样式的写入

    wb.save(file_path)


# 写入数据到txt
def Write2Txt(file_path, contents):
    f = open(file_path, mode='a+', encoding='utf-8')
    for i in range(len(contents)):
        f.write(contents[i] + '\n')
    f.close()


if __name__ == '__main__':
    # 切换到当前执行文件的工作目录下
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    os.chdir(abspath)

    file_path = abspath + "/test.csv"
    Write2CSV(file_path, ["姓名","年龄","性别"], [["l",'18','男'],["c",'20','男'],["w",'22','女']])

    file_path = abspath + "/test.txt"
    Write2Txt(file_path, ["aaaa","bbbb"])

    file_path = abspath + "/test.xls"
    Write2Excel(file_path, "test", [["a","b"],["1","2"],["4","5"]])