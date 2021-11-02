import xlrd
import xlwt

header_font = xlwt.Font()
header_font.bold = True
header_font.height = 12 * 20
header_font.name = '微软雅黑'
header_style = xlwt.XFStyle()
header_style.font = header_font


def write_excel(filename: str, headers: list, rows: list = None):
    """
    生成表格
    :param filename: 文件完整路径名
    :param headers: 表头
    :param row: 所有行数据
    """
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('Sheet1')
    if not filename or not headers:
        print('文件完整路径名或表头不能为空')
        return None
    # 生成表头
    for i in range(len(headers)):
        sheet.col(i).width = 200 * 30
        sheet.write(0, i, headers[i], header_style)
    # 填充数据
    if rows:
        for row_index in range(len(rows)):
            row = rows[row_index]
            for col_index in range(len(row)):
                sheet.write(row_index + 1, col_index, row[col_index])
    # 保存
    wb.save(filename)


def read_excel(filename: str):
    """
    读取excel
    :param filename: 文件完整路径名
    :return: 所有行数据，以字典的格式返回
    """
    if not filename:
        print('文件完整路径名不能为空')
        return None
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    headers = sheet.row_values(0)
    total_row_num = sheet.nrows
    total_col_num = sheet.ncols
    all_row = []
    for row_index in range(1, total_row_num):
        row = sheet.row_values(row_index)
        if _any_col_is_not_empty(row):
            all_row.append({headers[col_index]: row[col_index] for col_index in range(total_col_num)})
    return all_row


def _any_col_is_not_empty(row):
    """
    判断任意一列是不是不为空
    :param row: 行数据
    :return: 任意一列不为空，则返回True
    """
    for col in row:
        if col:
            return True
    return False


if __name__ == '__main__':
    write_excel('../../temp_file/test.xls', ['用户名', '密码', '性别'], [('张三', '123456', 'M'), ('李四', '123456789', 'F')])
    print(read_excel('../../temp_file/test.xls'))
