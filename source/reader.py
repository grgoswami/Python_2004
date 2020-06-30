
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
        with open(self.filepath, 'r') as infile:
            self.lines = infile.readlines()
            print(self.lines)
    
    def create_data_frame_from_lines_(self):
        self.set_header_()
        self.set_rows_()
        return None
    
    def set_header_(self):
        # The following process of splitting the header line 
        # into the column names is also called parsing the 
        # header line
        header_line = self.lines[0]
        self.columns = header_line.split(self.separator)
        print(self.columns)
        # List comprehension: create a list by doing col.trim()
        # for each element of the list self.columns
        self.columns = [col.strip() for col in self.columns]
        print(self.columns)
        
    def set_rows_(self):
        self.cells = {}
        for col in self.columns:
            self.cells[col] = []
        print(self.cells)
        for line in self.lines[1:]:
            print(line)
            values = line.split(self.separator)
            values = [val.strip() for val in values]
            print(values)
            for column_number, column in enumerate(self.columns):
                self.cells[column].append(values[column_number])
        print(self.cells)
            
        
        
        