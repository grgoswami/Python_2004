import reader

# Designing the 'interface' to solve the problem that we have 
reader0 = reader.XSV_Reader(separator=',')
data = reader0.read(r'/home/gopi/Python_202004/data/corona/ourworldindata/full_data.csv')
data.head()
