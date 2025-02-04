import sys

class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error = error
        _,_,tb = error_detail.exc.info()
        self.filename= tb.tb_frame.f_code.co_filename
        self.linenumber= tb.tb.lineno

    def __str__(self):
        return f'The "Error" {self.error}, occured in "File" {self.filename}, in line {self.linenumber}'



