import os

from data.operators.getContent import ExcelOperator

"""
对外开放API接口

"""


def get_plain_text(column):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'excel', 'comments.xlsx')
    excel_operator = ExcelOperator(file_path)
    text_in_column = excel_operator.load_context_in_columns(column)
    combined_text = text_in_column.str.cat(sep='')
    return combined_text


def get_plain_text_column4():
    return get_plain_text(4)


def get_single_text_in_column(row, column):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'excel', 'comments.xlsx')
    excel_operator = ExcelOperator(file_path)
    text_in_column = excel_operator.load_context_by_one(row, column)
    combined_text = text_in_column.str.cat(sep='')
    return combined_text





print(get_plain_text_column4())