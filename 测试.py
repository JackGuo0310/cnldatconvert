import time


def process_large_file(input_file, output_file):
    # 打开输入和输出文件
    with open(input_file, 'r') as f_input, open(output_file, 'w') as f_output:
        # 逐行读取输入文件
        row=1
        line_num=0
        for line in f_input:
            if line_num==row:
                line_list=line.split('\t')
                print(line_list)
                # print(type(line))
                # print(list(line))
                # print(type(line))
                # 处理需要修改的那一行
                # if '需要修改的内容' in line:
                #     line = line.replace('需要修改的内容', '新内容')
                # 将处理后的行写入输出文件
                # time.sleep(0.1)
            f_output.write(line)
            break


input_file = 'D:\IDM下载\中汽研dat文件改名测试\Dece-E-Stop.dat'
output_file = 'D:\IDM下载\中汽研dat文件改名测试\shengcheng.dat'
process_large_file(input_file, output_file)


# 需要一个新函数,给一个行代表的字符串, 给两个列表,更改值,返回更改后的字符串
def update_line(line_str,chn_list,cn_list):
    line_list = line_str.split('\t').strip()
    print(line_list)
    print(chn_list)
    print(cn_list)
    for channel_name in chn_list:
        try:
            index=line_list.index(channel_name)
            # i=chn_list.index(channel_name)
            line_list[index]=cn_list[chn_list.index(channel_name)]
        except Exception:
            pass
    str=''
    for sub_line_list in line_list:
        str=str+sub_line_list+'\t'
    str=str+'\n'

    print(str)
    return str