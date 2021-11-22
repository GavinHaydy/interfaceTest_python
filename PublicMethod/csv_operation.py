import csv


class ReadCSV:
    def get_value(self, row_num, col_num):
        with open(self, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]
            return rows[row_num][col_num]


'''
    from csv_operation import ReadCSV
    ReadCSV.get_value(path,row_num,col_num)
'''


