import os

from data.operators.getContent import ExcelOperator

"""
对外开放API接口

"""


def load_file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'excel', 'commentsLH.xlsx')
    excel_operator = ExcelOperator(file_path)
    return excel_operator


def get_plain_text(column):
    excel_operator = load_file()
    text_in_column = excel_operator.load_context_in_columns(column)
    combined_text = text_in_column.str.cat(sep='')
    return combined_text


def get_plain_text_column4():
    return get_plain_text(4)


def get_single_text_in_column(row, column):
    excel_operator = load_file()
    text_in_column = excel_operator.load_context_by_one(row, column)
    return text_in_column


def get_single_text_in_column4(row):
    return get_single_text_in_column(row, 4)


def get_num_rows():
    excel_operator = load_file()
    return excel_operator.get_num_rows()

# print(get_single_text_in_column4(3))
# print(get_plain_text_column4())
# print(get_num_rows())
