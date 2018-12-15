import xlrd
from xlutils.copy import copy
import os

# ============================================
# 对excel进行封装
# 从excel文件中读取测试用例
# 向Excel写入测试结果
# ============================================

# 获取上级目录
# print(os.path.abspath(os.path.dirname(os.getcwd())))
test_data_dir = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "testdata")
#print(test_data_dir)

class DoExcel():

    def __init__(self, file_name, sheet_name):
        '''
        初始化excel文件对象
        :param file_name: excel文件名
        :param sheet_name: sheet名
        '''
        self.file_name = os.path.join(test_data_dir, file_name);
        self.workbook = xlrd.open_workbook(self.file_name)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_row_num(self, cols_num, case_id):
        '''
        获取指定测试用例id对应的行号
        :param cols_num: 测试用例id所在的列号
        :param case_id: 指定的测试用例id
        :return: 
        '''
        # 获取指定列的所有的值
        cols = self.sheet.col_values(cols_num)

        row_num = 0
        for col_data in cols:
            if col_data == case_id:
                break
            row_num += 1
        return row_num

    def get_rowline_data(self, row):
        '''
        获取某一行的值
        :param row: 
        :return: 
        '''
        return self.sheet.row_values(row)

    def read_cell(self, row_num, col_num):
        return self.sheet.cell(row_num, col_num).value

    def write_excel(self, sheetnum, row, col, value):
        '''
        向excel中写数据
        :param sheetnum: sheet索引 
        :param row: 行索引
        :param col: 列索引
        :param value: 要写入的值
        :return: 
        '''
        new_workbook = xlrd.open_workbook(self.file_name)
        new_wbook = copy(new_workbook)
        sheet = new_wbook.get_sheet(sheetnum)

        sheet.write(row, col, value)
        new_wbook.save(self.file_name)

# =============================================================
# 测试代码，验证DoExcel的正确性
# =============================================================

if __name__ == "__main__":
    excel = DoExcel("case.xls", "Sheet1")
    row = excel.get_row_num(0, "bd-001")
    print(row)
    row_data = excel.get_rowline_data(row)
    print(row_data)
    print("=============================")

    excel.write_excel(0, 1, 6, "test")
    # 问题：为什么这里取到的是修改之前的值
    row_data1 = excel.get_rowline_data(row)
    print(row_data1)
