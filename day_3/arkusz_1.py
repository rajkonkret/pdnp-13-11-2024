import pandas as pd
import numpy as np
import openpyxl

technologies = ['Spark', "Pandas", "Python", "PHP"]
feee = [25000, 20000, 15000, 22000, 18000]
discount = [2000, 1500, 800, 500, 500]
duration = ['50 Days', '30 Days', np.nan, '15 Days']

columns = ['Courses', 'Fee', 'Duration', 'Discount']

df = pd.DataFrame(list(zip(technologies, feee, duration, discount)), columns=columns)
print(df)
#   Courses    Fee Duration  Discount
# 0   Spark  25000  50 Days      2000
# 1  Pandas  20000  30 Days      1500
# 2  Python  15000      NaN       800
# 3     PHP  22000  15 Days       500

df.to_excel('courses.xlsx')

excel_data = pd.read_excel('courses.xlsx')
print(excel_data)
#    Unnamed: 0 Courses    Fee Duration  Discount
# 0           0   Spark  25000  50 Days      2000
# 1           1  Pandas  20000  30 Days      1500
# 2           2  Python  15000      NaN       800
# 3           3     PHP  22000  15 Days       500

data = pd.DataFrame(excel_data)
print(data.columns)  # Index(['Unnamed: 0', 'Courses', 'Fee', 'Duration', 'Discount'], dtype='object')
