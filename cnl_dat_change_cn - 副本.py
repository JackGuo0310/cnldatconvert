# import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
# import chardet
import csv

import shutil
import time
import os
import icon,os,base64
from icon import Icon

# cnl_CHN_list = []
# cnl_CN_list = []


def select_file1():
    file_path = filedialog.askopenfilename(filetypes=[("cnl Files", "*.cnl")])
    if file_path:
        entry1.delete(0, END)
        entry1.insert(0, file_path)
    else:
        entry1.delete(0, END)
        entry1.insert(0, "未选择文件，请选择文件")


def select_file2():
    file_path = filedialog.askopenfilename(filetypes=[("dat Files", "*.dat")])
    if file_path:
        entry2.delete(0, END)
        entry2.insert(0, file_path)
    else:
        entry2.delete(0, END)
        entry2.insert(0, "未选择文件，请选择文件")


# 定义函数，将指定的cnl文件转化为两个列表，分别是cnl_CHN_list(通道名列表)  cnl_CN_list(客户名列表)
def op_cnl_to_list(cnl_file_name):
    cnl_chn_list_1 = []
    cnl_cn_list_1 = []
    # 获取文件编码方式
    # with open(cnl_file_name, "rb") as f:
    #     data = f.read()
    #     result = chardet.detect(data)
    #     encoding = result["encoding"]
    #     print(encoding)

    with open(cnl_file_name, 'r', encoding='utf-8') as cnl:
        # cnl.seek(0)
        try:
            lines = cnl.readlines()
            # print(lines)
        except UnicodeDecodeError:
            alert('警告', 'cnl文件解析不正确,可能是内容存在中文')
            return False
        # list_len = len(lines)
        for i in range(len(lines)):
            if lines[i].strip().split(',')[1] != '':
                cnl_chn_list_1.append(lines[i].strip().split(',')[0][:-3])
                cnl_cn_list_1.append(lines[i].strip().split(',')[1])
    del cnl_chn_list_1[0]
    del cnl_cn_list_1[0]
    # print(cnl_chn_list_1)
    # print(cnl_cn_list_1)
    return cnl_chn_list_1, cnl_cn_list_1


# 定义函数，在给的dat文件里面的第row_num行寻找字符串search_str，找到的话返回对应的列数，没找到，返回-9999,如果没有给定的行数，返回-10000
def find_cell(filename, search_str, row_num):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            # print(row)
            if i == int(row_num) - 1:
                # print(row)
                new_list = row[0].strip().split('\t')
                try:
                    index = new_list.index(search_str)
                    # 返回列数，从1开始，需要加1显示
                    # print(index+1)
                    return index + 1
                except ValueError:
                    # print(-9999)
                    return -9999

        # print(-10000)
        return -10000


# 返回关键词对应的行数，如果都没找到，返回-9999. 只找前1000行
def op_find_need_change_line(filename, key_name):
    j = 1000
    i = 1
    while i <= j:
        row = find_cell(filename, key_name, i)
        if row != -9999 and row != -10000:
            # print(i)
            return i
        i += 1
    # print(i)
    return -9999


# 复制给定文件，另存为新文件，文件名加上当前时间,返回新文件的路径
def copy_file_with_date_time(src_file_path):
    filename, file_extension = os.path.splitext(src_file_path)
    dst_file_path = filename + "_" + time.strftime("%Y%m%d_%H%M%S") + file_extension
    try:
        shutil.copy2(src_file_path, dst_file_path)
        return dst_file_path
    except Exception:
        return 'None_-999_must_No_body_use_it_be_a_filename'


# 更新row_index行，column_index列的值
def update_csv_cell(file_path, row_index, column_index, new_value):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,'1')
    new_list = data[row_index][0].strip().split('\t')

    new_list[column_index] = new_value

    new_list1 = ['']

    string1 = ''
    for str1 in new_list:
        string1 = string1 + str1 + '\t'
    string1 = string1.strip('\t')
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,'2')
    new_list1[0] = string1
    data[row_index] = new_list1
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,'3')

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,'4')

# 弹窗警告
def alert(title, message):
    messagebox.showwarning(title, message)


# OK弹窗
def mess_ok(title, message):
    messagebox.showinfo(title, message)


# 判断文件是否合法
def is_file_path_valid(file_path, file_extension):
    # 判断文件是否真实存在
    if os.path.isfile(file_path):
        # 判断文件后缀是否与所需的文件后缀一致
        if file_path.endswith(file_extension):
            return True
    return False


def main_modify_dat_file(key_name_use_to_find_location_row):
    # cnl_chn_list = []
    # cnl_cn_list = []
    cnl_file_really = entry1.get()

    dat_file_choose = entry2.get()

    if is_file_path_valid(cnl_file_really, '.cnl') is False:
        alert('警告', '未选择正确的cnl文件')
        return None

    if is_file_path_valid(dat_file_choose, '.dat') is False:
        alert('警告', '未选择正确的dat文件')
        return None

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'cnl文件路径{cnl_file_really}')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'dat文件路径{dat_file_choose}')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,'正在查找Alias对应的行数')
    row = op_find_need_change_line(dat_file_choose, key_name_use_to_find_location_row)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'行数是{row}')

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'.cnl文件转化为列表')
    if op_cnl_to_list(cnl_file_really) is False:
        return False
    else:
        cnl_chn_list, cnl_cn_list = op_cnl_to_list(cnl_file_really)
    done_num = 0
    total_num = len(cnl_chn_list)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'列表转化完成,一共{total_num}个变量需要改名')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,cnl_chn_list)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,cnl_cn_list)

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,'正在复制数据文件...')
    dat_file_finally = copy_file_with_date_time(dat_file_choose)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'最终dat文件名为{dat_file_finally}')

    if dat_file_finally == 'None_-999_must_No_body_use_it_be_a_filename':
        alert('警告',
              '可能本软件没有权限在当前路径写入文件,请尝试把dat文件换一个路径,一般发生在dat文件在C盘或者任一盘符的根目录下,或者尝试使用管理员身份运行.')
        return None
    # print(cnl_chn_list)
    # print(cnl_cn_list)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,'正在处理,请等待...')
    for channel_name in cnl_chn_list:
        column = find_cell(dat_file_finally, channel_name, row)
        # 大于-1表示找到了
        if column > -1:
            done_num += 1
            chn_index = cnl_chn_list.index(channel_name)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'正在更改第{chn_index+1}个变量')
            update_csv_cell(dat_file_finally, row - 1, column - 1, cnl_cn_list[chn_index])

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  ,f'处理完成,共{total_num}个变量,完成{done_num}个变量.')
    mess_ok('提示', f'处理完成,共{total_num}个变量,完成{done_num}个变量.')


root = Tk()
root.title("处理数据")

with open('tmp.ico','wb') as tmp:
    tmp.write(base64.b64decode(Icon().img))

root.iconbitmap('tmp.ico')
os.remove('tmp.ico')
root.geometry("500x300")


button1 = Button(root, text="选择cnl文件", width=10, height=1, command=select_file1)
button1.place(x=50, y=50)
#
button2 = Button(root, text="选择dat文件", width=10, height=1, command=select_file2)
button2.place(x=50, y=100)

entry1 = Entry(root)
entry1.place(x=150, y=50, width=300, height=28)
entry1.insert(0, "未选择文件，请选择文件")
#
entry2 = Entry(root)
entry2.place(x=150, y=100, width=300, height=28)
entry2.insert(0, "未选择文件，请选择文件")

txt1 = Label(root, text='生成文件的路径与dat文件路径一致', width=10, height=1)
txt1.place(x=150, y=150, width=200, height=28)

button3 = Button(root, text="一键生成", width=10, command=lambda: main_modify_dat_file('Alias'))
button3.place(x=50, y=150)

# button4 = Button(root, text="测试函数", width=10, command=lambda: op_cnl_to_list('C:\ADT\iTest4.1BTS\Solution.Battery_GK_keyi_ceshi_gongneng\CanNeo1_HS1.cnl'))
# button4.place(x=50, y=200)

root.mainloop()
