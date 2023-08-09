import os

from data.operators.getContent import ExcelOperator

"""
对外开放API接口
"""


def load_file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'excel', 'comments.xlsx')
    excel_operator = ExcelOperator(file_path)
    return excel_operator


class LoadData:
    def __init__(self):
        self.content = load_file()

    def get_plain_text(self, column):
        excel_operator = self.content
        text_in_column = excel_operator.load_context_in_columns(column)
        combined_text = text_in_column.str.cat(sep='')
        return combined_text

    def get_plain_text_column4(self):
        return self.get_plain_text(4)

    def get_single_text_in_column(self, row, column):
        excel_operator = self.content
        text_in_column = excel_operator.load_context_by_one(row, column)
        return text_in_column

    def get_single_text_in_column4(self, row):
        return self.get_single_text_in_column(row, 4)

    def get_num_rows(self):
        excel_operator = self.content
        return excel_operator.get_num_rows()

# print(get_single_text_in_column4(3))
# print(get_plain_text_column4())
# print(get_num_rows())
