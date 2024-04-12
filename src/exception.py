import sys
#from logger import *

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()

    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="Error occured in python script name [{0}], line number: [{1}], error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
        )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message=error_message
    
    def get_error_details(self, error_detail):
        self.error_message=error_message_detail(self.error_message, error_detail=error_detail)
        return self.error_message

'''
if __name__=="__main__":
    try:
        a=5/0
    except Exception as e:
        
        ce=CustomException(e)
        error_message=ce.get_error_details(sys)
        print(error_message)
        logger.info(error_message)
'''