import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
        Extracts detailed error information including file name, line number, and the error message.

        :param error: The exception that occurred.
        :param error_detail: The sys module to access traceback details.
        :return: A formatted error message string.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number: [{line_number}] with error message: {error}"
    logging.error(error_message)

    return error_message
class MyException(Exception):

    def __init__(self, error_message: Exception, error_detail: sys):

        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message