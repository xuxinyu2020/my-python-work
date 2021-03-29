# mxj提供API获取脚本
# def get_ip():
#     params = {
#         "name": 'limit',
#         "in": 'query',
#         "description": 2,
#         "type": 'string',
#     }
#     data = json.dumps(params).replace(' ', '')
#     res = requests.get(url, data=data, headers=headers)
#     module_info = json.loads(res.content)
#     print(module_info)
import xlrd
import xlwt
import requests
import json

url = "http://10.1.8.70:11000/os/image/v1/v2/images"

headers = {"Content-Type": "application/json",
           "Accept": "application/json",
           "X-Auth-Token": "gAAAAABgYVJXgpV11sARIVnKZER0OSoMIZCDBK6kn-_nrfD4WpQg71O8VwT5s8m5oLU-hHXZguSwhLI0fCH5Wu8UHhv_pyd_2JfQNj-Y8P6SUc35rHRHp6PNhcIcDLjlW2NYAMhvJCMejgCn3WhIXI3MOQOHMHPC4Zb4H6pZK0M2-wIOkOiisEM"
           }


def request_image(url,json_file_saved):
    '''请求镜像列表API获取json数据保存至文件,url请求API，json_file_saved要保存的json文件名'''
    response = requests.get(url, headers=headers).json()
    with open(json_file_saved, 'w') as f:
        json.dump(response, f)


def json_into_txt(file):
    '''将json文件提取转化为txt文件，file要处理的json文件'''
    json_file = file
    with open(json_file, 'r', encoding='utf-8') as f2:
        response_json = json.load(f2)
        # print(response_json)
        n = 0
        images_dict = response_json['images']
        for image in images_dict:
            ex_para = 1073741824
            uuid = image['id']
            size_o = image['size']
            name = image['name']
            # size = round(size_o/ex_para,2)
            new_str = uuid + ' ' + str(size_o) + ' ' + name
            with open('images_info.txt', 'a') as f3:
                f3.writelines(new_str + '\n')  # 用于换行
            n = n + 1
    print(f'成功完成{n}个镜像的信息导出！')


def image_excel(file,excel_file_save):
    '''将镜像信息转化成excel表格 file要处理的json文件名'''
    file_name = file
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('glance镜像信息')

    # 编辑表头
    titles = ['序号', 'uuid', '镜像名', '镜像大小']
    for index, title in enumerate(titles):
        sheet.write(0, index, title)

    # json数据写入list
    with open(file_name, 'r', encoding='utf-8') as f2:
        response_json = json.load(f2)
        # print(response_json)
        n = 0
        lines = []
        images_dict = response_json['images']
        for image in images_dict:
            new_line = []
            uuid = image['id']
            new_line.append(uuid)
            name = image['name']
            new_line.append(name)
            size_o = image['size']
            new_line.append(size_o)
            lines.append(new_line)

        # print(lines)
    # 列表数据写入单元格
    for row in range(len(lines)):
        sheet.write(row + 1, 0, row + 1)
        for col in range(len(lines[row])):
            sheet.write(row + 1, col + 1, lines[row][col])

    # 保存数据
    wb.save(excel_file_save)
    print("成功写入excel表格！")


def generate_uuid_to_name(file_name):
    '''根据镜像名字，查找到对应的uuid，并附加到前一列 file要遍历查询的镜像excel表'''
    # 遍历读取源excel里的镜像名，并保存为列表
    wb = xlrd.open_workbook('靶标、场景镜像名称.xls')
    sheets = wb.sheet_names()
    new_workbook = xlwt.Workbook()  # 新建一个工作簿对象，用于存放结果
    file = file_name
    for sheet in sheets:
        list = []
        image_sheet = wb.sheet_by_name(sheet)
        print(f'{sheet}加载成功！')
        for row in range(1, image_sheet.nrows):
            list.append(image_sheet.cell(row, 1).value.strip())

        # 在glance镜像表中遍历查找镜像名对应的uuid
        glance_info_sheet = xlrd.open_workbook(file).sheet_by_index(0)
        uuid_to_name_sheet = new_workbook.add_sheet(sheet)  # 增加一个以原sheet为名的sheet
        for index, image_name in enumerate(list):
            flag = 0
            for glance_row in range(1, glance_info_sheet.nrows):
                try:
                    if glance_info_sheet.cell(glance_row, 2).value == image_name:
                        uuid = glance_info_sheet.cell(glance_row, 1).value
                        uuid_to_name_sheet.write(index, 0, uuid)
                        uuid_to_name_sheet.write(index, 1, image_name)
                        flag = 1
                        continue
                except:
                    continue
            if flag == 0:
                print(f'表{sheet} 序列号{index + 1} {image_name}未查询到uuid')

    new_workbook.save('镜像导出列表2.xls')


def main():
    # request_image(url,'images2.json')
    image_excel('images2.json','glance镜像信息表2.xls')
    generate_uuid_to_name('glance镜像信息表2.xls')


if __name__ == '__main__':
    main()
