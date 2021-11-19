import xlrd


class ReadExcel:
    def __init__(self, path, sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_value(self, row, col):
        sheet_value = self.sheet.cell_value(row, col)
        if sheet_value == "":
            return "此单元格无数据"
        else:
            return sheet_value
    """ from PublicMethod.excel_operation import ReadExcel
        file = ReadExcel(path, sheet_name)
        print(file.get_value(row, col))
        
        if file is '*.xslx' please install xlrd==1.2.0
    """