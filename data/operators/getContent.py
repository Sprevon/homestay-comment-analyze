import os
import pandas as pd

"""
获取excel数据并拼接

"""


class ExcelOperator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = self.load_workbook()

    def load_workbook(self):
        try:
            return pd.read_excel(self.file_path, sheet_name='sheet1')
        except Exception as e:
            raise ValueError("Error loading data from Excel:", e)

    def load_context_in_columns(self, column):
        try:
            value = self.workbook.iloc[:, column]
            return value
        except Exception as e:
            raise ValueError("Error loading colum context from workbook:", e)

    def load_context_in_row(self, row):
        try:
            value = self.workbook.iloc[row, :]
            return value
        except Exception as e:
            raise ValueError("Error loading row context from workbook:", e)

    def load_context_by_one(self, row, column):
        try:
            value = self.workbook.iloc[row, column]
            return value
        except Exception  as e:
            raise ValueError("Error loading single context from workbook:", e)

    def get_num_rows(self):
        try:
            value = self.workbook.shape[0]
            return value
        except Exception as e:
            raise ValueError("Error loading num_rows from workbook:", e)



# current_directory = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_directory, '..', 'excel', 'commentsL.xlsx')
# excel_operator = ExcelOperator(file_path)
# print(excel_operator.load_context_in_columns(4))
# print("\n", excel_operator.load_context_by_one(1, 4))
# print(excel_operator.get_num_rows())