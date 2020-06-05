
import pandas

# For now let's only consider three kinds of separators: , or \t or |
class XSV_Reader:
    def __init__(self, separator=','):
        self.separator = separator
        
    def read(self, filepath):
        self.filepath = filepath
        print('Will read from: filepath=' + filepath)
        return pandas.read_csv(self.filepath, sep=self.separator)