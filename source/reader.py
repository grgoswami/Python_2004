
import pandas

# For now let's only consider three kinds of separators: , or \t or |
class XSV_Reader:
    def __init__(self, separator=','):
        self.separator = separator
        
    def read_using_pandas(self, filepath):
        self.filepath = filepath
        print('Will read from: filepath=' + filepath)
        return pandas.read_csv(self.filepath, sep=self.separator)
    
    # Functions that solve sub problems and are not part of the 
    # interface should have an '_' in the end, this reminds you
    # that these are helper functions
    def read(self, filepath):
        self.filepath = filepath
        print('Will read from: filepath=' + filepath)
        self.read_lines_from_file_()
        return self.create_data_frame_from_lines_()
    
    def read_lines_from_file_(self):
        pass
    
    def create_data_frame_from_lines_(self):
        return None
    
        